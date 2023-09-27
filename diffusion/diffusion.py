import matplotlib.pyplot as plt

grid_shape = (640, 640) # a global variable for (lazy) convenience

def evolve(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    new_grid = [[0.0 for x in range(grid_shape[1])] for x in range(grid_shape[0])]
    for i in range(xmax):
        for j in range(ymax):
            grid_xx = (
                grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            )
            new_grid[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
    return new_grid


def run_experiment(num_iterations):
    # setting up initial conditions
    grid = [[0.0 for x in range(grid_shape[1])] for x in range(grid_shape[0])]

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    # evolve grid
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)

    return grid

# This file could either be run as a script or used as a module
# The following code will only be executed if this file
# is treated as a script

if __name__ == "__main__":
    result = run_experiment(500)

    p = plt.pcolormesh(result)
    cb = plt.colorbar(p)
    plt.xlabel("Grid X Index")
    plt.ylabel("Grid Y Index")
    cb.set_label("Concentration")
    plt.savefig("diffusion.png")
