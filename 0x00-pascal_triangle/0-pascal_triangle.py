#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []
    
    # Initialize the triangle list
    triangle = []

    # Iterate through the number of rows
    for i in range(n):
        # First value in each row is always 1
        row = [1]

        # For all rows except the first row, calculate the values
        if i > 0:
            for j in range(i-1):
                # Calculate the value for each index by adding the values from the previous row
                row.append(triangle[i-1][j] + triangle[i-1][j+1])

            # Last value in each row is always 1
            row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    # Return the final triangle
    return triangle
