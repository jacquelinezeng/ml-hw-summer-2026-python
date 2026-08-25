import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_binary_value(prompt):
    while True:
        try:
            value=int(input(prompt))
            if value in [0, 1]:
                return value
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

def main():
    while True:
        try:
            n=int(input('Enter N: '))
            if n>0:
                break
            print('N must be greater than 0.')
        except ValueError:
            print('Please enter a positive integer.')

    actual=np.zeros(n, dtype=int)
    predicted=np.zeros(n, dtype=int)

    for i in range(n):
        print(f"Point {i+1}")
        actual[i]=read_binary_value("Enter x value, the correct class, 0 or 1: ")
        predicted[i]=read_binary_value("Enter y value, the predicted class, 0 or 1: ")


    precision=precision_score(actual, predicted, zero_division=0)
    recall=recall_score(actual, predicted, zero_division=0)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

main()
            