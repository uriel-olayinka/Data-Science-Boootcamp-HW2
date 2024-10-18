import numpy as np

A = np.array([1, 2, 3, 4, 5, 6])
B = np.array([7, 8, 9, 10, 11, 12])

#Q1
v_stack = np.vstack((A, B))
h_stack = np.hstack((A, B))

print("Vertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)

print()

#Q2
common = np.intersect1d(A, B)
print("Common elements:", common)

print()

#Q3
between_5_and_10 = A[(A >= 5) & (A <= 10)]
print("Numbers from A between 5 and 10:", between_5_and_10)

print()

#Q4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

filtered_iris2d = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
print("Filtered Iris 2D:\n", filtered_iris2d)