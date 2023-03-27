#!/usr/bin/python3
# 0. Island Perimeter


def island_perimeter(grid):
    # initialize land and adj variables
    land = 0
    adj = 0
    # loop over the rows of the grid
    for i in range(len(grid)):
        # loop over the columns of the grid
        for j in range(len(grid[i])):
            # if the cell is land
            if grid[i][j] == 1:
                # increment land by 1
                land += 1
                # if the cell below is also land
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    # increment adj by 1
                    adj += 1
                # if the cell to the right is also land
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    # increment adj by 1
                    adj += 1
    # return the perimeter formula
    return 4 * land - 2 * adj
