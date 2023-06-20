# Island Perimeter

This is a Python function that calculates the perimeter of an island described in a grid.

## Description

The function `island_perimeter(grid)` takes a grid as input and returns the perimeter of the island. The grid is represented as a list of lists, where 0 represents water and 1 represents land. Each cell in the grid is square with a side length of 1. The cells are connected horizontally and vertically (not diagonally). The grid is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water, and there is only one island (or nothing). The island doesn't have any "lakes" (water inside that isn't connected to the water surrounding the island).

## Usage

To use the function, provide a grid as a list of lists and call the `island_perimeter(grid)` function. The function will return the perimeter of the island.

Example usage:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
