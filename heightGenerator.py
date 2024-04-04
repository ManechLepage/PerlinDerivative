import opensimplex
import random


def generate_2d_grid(size, scale=1, seed=1):
    noise = opensimplex.OpenSimplex(seed)
    grid = []
    for x in range(size[0]):
        row = []
        for y in range(size[1]):
            row.append(noise.noise2(x / scale, y / scale))
        grid.append(row)
    return grid


def initialize_grid(size, layers=[15, 8, 2]):
    layers = [l * (size[0] / 64) for l in layers]
    grid = generate_2d_grid(size, scale=layers[0], seed=random.randint(0, 10000))
    for layer in range(len(layers) - 1):
        tmp_grid = generate_2d_grid(size, scale=layers[layer - 1], seed=random.randint(0, 100000))
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid[x][y] += tmp_grid[x][y] * (0.1 * (1 / (layer + 1)))
    return grid
