#!/usr/bin/python3
# Island Perimeter


def island_perimeter(grid):
    """
    function that returns the perimeter of the island
    described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  
                # Start with the assumption of a full perimeter

                # Check adjacent cells and reduce the perimeter accordingly
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
