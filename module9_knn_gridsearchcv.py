import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid real number.")


def read_dataset(number_of_pairs, dataset_name):
    x_values = np.empty((number_of_pairs, 1), dtype=float)
    y_values = np.empty(number_of_pairs, dtype=int)

    for index in range(number_of_pairs):
        pair_number = index + 1
        x_values[index, 0] = read_real_number(
            f"Enter x value for {dataset_name} pair {pair_number}: "
        )
        y_values[index] = read_non_negative_integer(
            f"Enter y class label for {dataset_name} pair {pair_number}: "
        )

    return x_values, y_values


def choose_best_knn_model(x_train, y_train):
    if len(x_train) == 1:
        model = KNeighborsClassifier(n_neighbors=1)
        model.fit(x_train, y_train)
        return model, 1

    candidate_k_values = list(range(1, min(10, len(x_train) - 1) + 1))

    grid_search = GridSearchCV(
        estimator=KNeighborsClassifier(),
        param_grid={"n_neighbors": candidate_k_values},
        cv=LeaveOneOut(),
        scoring="accuracy",
    )

    grid_search.fit(x_train, y_train)

    return grid_search.best_estimator_, grid_search.best_params_["n_neighbors"]


def main():
    n = read_positive_integer("Enter N, the number of training pairs: ")
    x_train, y_train = read_dataset(n, "training")

    m = read_positive_integer("Enter M, the number of test pairs: ")
    x_test, y_test = read_dataset(m, "test")

    best_model, best_k = choose_best_knn_model(x_train, y_train)

    predictions = best_model.predict(x_test)
    test_accuracy = accuracy_score(y_test, predictions)

    print(f"Best k: {best_k}")
    print(f"Test accuracy: {test_accuracy:.4f}")

main()