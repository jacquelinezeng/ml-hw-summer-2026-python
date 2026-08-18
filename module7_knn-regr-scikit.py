import numpy as np 
from sklearn.neighbors import KNeighborsRegressor

N=int(input('Enter N, the number of training points: '))

k=int(input('Enter k, the number of nearest neighbors: '))

if N<=0 or k<=0:
    print('Error: N and k must be positive intergers')

elif k>N:
    print('Error: k cannot be greater than N')

else:
    X_train=np.empty((N,1))
    y_train=np.empty(N)

    for i in range(N):
        print(f'Enter point {i+1}: ')
        x=float(input('x: '))
        y=float(input('y: '))

        X_train[i,0]=x 
        y_train[i]=y 

    X_value=float(input('Enter X value for prediction: '))

    model=KNeighborsRegressor(n_neighbors==k)
    model.fit(X_train, y_train)

    predicted_y=model.predict(np.array([[X_value]]))
    label_variance=np.var(y_train)

    print('Predicted Y: ', predicted_y[0])
    print('Variance of labels in training dataset: ', label_variance)



