import numpy as np


def read_positive_integer(prompt):
    value = int(input(prompt))

    while value <= 0:
        print("Error: please enter a positive integer.")
        value = int(input(prompt))

    return value


def main():
    n = read_positive_integer("Enter N, a positive integer: ")
    k = read_positive_integer("Enter k, a positive integer: ")

    points = np.zeros((n, 2))

    for i in range(n):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points[i] = [x, y]

    x_input = float(input("Enter X value to predict Y: "))

    if k > n:
        print("Error: k cannot be greater than N.")
        return

    x_values = points[:, 0]
    y_values = points[:, 1]

    distances = np.abs(x_values - x_input)
    nearest_indexes = np.argsort(distances)[:k]
    nearest_y_values = y_values[nearest_indexes]

    predicted_y = np.mean(nearest_y_values)

    print("Predicted Y:", predicted_y)


main()