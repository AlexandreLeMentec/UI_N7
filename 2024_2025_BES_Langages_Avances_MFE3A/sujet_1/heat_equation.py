import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from json import dumps, load

print("2D heat equation solver")

# Loading inputs
with open("heat_equation_inputs.json", mode='r') as json_file:
    dict_inputs = load(json_file)


# Setting parameters
max_iter_time = int(dict_inputs['TIME_STEPS'])

lx = dict_inputs['DIMENSIONS']['lx']
ly = dict_inputs['DIMENSIONS']['ly']
nx = int(dict_inputs['MESH']['nx'])
ny = int(dict_inputs['MESH']['ny'])

alpha = dict_inputs['HEAT_DIFF_COEF']

delta_x = lx/nx
delta_y = ly/ny

delta_t = (np.minimum(delta_x, delta_y) ** 2)/(4 * alpha)

gamma_x = (alpha * delta_t) / (delta_x ** 2)
gamma_y = (alpha * delta_t) / (delta_y ** 2)


# Initialize solution: the grid of u(k, i, j)
u = np.empty((max_iter_time, nx, ny))


# Initial condition everywhere inside the grid
u_initial = dict_inputs['INITIAL_CONDITION']


# Boundary conditions
u_top_type = dict_inputs['YMAX_BOUNDARY']['type']
u_top_value = dict_inputs['YMAX_BOUNDARY']['value']
u_left_type = dict_inputs['XMIN_BOUNDARY']['type']
u_left_value = dict_inputs['XMIN_BOUNDARY']['value']
u_bottom_type = dict_inputs['YMIN_BOUNDARY']['type']
u_bottom_value = dict_inputs['YMIN_BOUNDARY']['value']
u_right_type = dict_inputs['XMAX_BOUNDARY']['type']
u_right_value = dict_inputs['XMAX_BOUNDARY']['value']


# Set the initial condition
u.fill(u_initial)


# Function to solve heat equation
def calculate(u):

    for k in range(0, max_iter_time-1, 1):
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u[k + 1, i, j] = gamma_x * (u[k][i+1][j] + u[k][i-1][j] - 2*u[k][i][j]) + gamma_y * (u[k][i][j+1] + u[k][i][j-1] - 2*u[k][i][j]) + u[k][i][j]

        # Set the boundary conditions
        if u_top_type=='Neumann':
            u[k + 1, (nx-1), :] = u_top_value*delta_y + u[k + 1, (nx-2), :]
        if u_top_type=='Dirichlet':
            u[k + 1, (nx-1), :] = u_top_value
        
        if u_left_type=='Neumann':
            u[k + 1, :, 0] = -u_left_value*delta_x + u[k + 1, :, 1]
        if u_left_type=='Dirichlet':
            u[k + 1, :, 0] = u_left_value
        
        if u_bottom_type=='Neumann':
            u[k + 1, 0, :] = -u_bottom_value*delta_y + u[k + 1, 1, :]
        if u_bottom_type=='Dirichlet':
            u[k + 1, 0, :] = u_bottom_value
        
        if u_right_type=='Neumann':
            u[k + 1, :, (ny-1)] = u_right_value*delta_x + u[k + 1, :, (ny-2)]
        if u_right_type=='Dirichlet':
            u[k + 1, :, (ny-1)] = u_right_value
	
    return u


# Do the calculation
u = calculate(u)


# Function to plot results
def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} s")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.imshow(u_k, cmap=plt.cm.jet, vmin=u.min(), vmax=u.max(), extent=[0,lx,0,ly],interpolation='gaussian',origin='lower')
    plt.xlim(0, lx)
    plt.ylim(0, ly)
    plt.colorbar()

    return plt


# Function make an animation
def animate(k):
    plotheatmap(u[k], k)


# Do the animation
anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
plt.show()


print("Done!")




