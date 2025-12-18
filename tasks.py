import numpy as np
#task1
# white = 0, light = 0.3, medium = 0.6, dark = 1.0

A = np.array([
    [0, 0.6, 0.3, 0.6],
    [0.6, 0.6, 0.6, 0.3],
    [0.3, 0.6, 0.6, 0.6],
    [0.6, 0.3, 0.6, 0]
])

B = np.array([
    [0.3, 0.3, 0, 0],
    [0.3, 0.3, 0, 0],
    [0.6, 0.6, 0.3, 0.3],
    [0.6, 0.6, 0.3, 0.3]
])

C = np.array([
    [0, 0, 0.3, 0.3],
    [0, 0, 0.3, 0.3],
    [0.3, 0.3, 0.6, 0.6],
    [0.3, 0.3, 0.6, 0.6]
])

D = np.array([
    [0.6, 0.6, 0.6, 0],
    [0.6, 0.6, 0.6, 0],
    [0.3, 0.6, 0.3, 0],
    [0.3, 0.6, 0.3, 0]
])

E = np.array([
    [0, 0.6, 0.6, 0.6],
    [0, 0.6, 0.6, 0.6],
    [0.3, 0.3, 0.6, 0],
    [0.3, 0.3, 0.6, 0]
])

F = np.array([
    [0.3, 0.6, 0, 0.6],
    [0.6, 0.3, 0.6, 0],
    [0, 0.6, 0.3, 0.6],
    [0.6, 0, 0.6, 0.3]
])

images = [A, B, C, D, E, F]

X = np.array([img.flatten() for img in images])

X_centered = X - X.mean(axis=1, keepdims=True)

U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

correlation_matrix = np.corrcoef(X)

print("Correlation matrix (A, B, C, D, E, F):")
print(np.round(correlation_matrix, 2))


#task2

V = np.array([1, 2, 5, -1, 3, 0, 5])
Bv = np.array([-4, 3, 0, -2, 2, 5, 1])


A = np.outer(V, Bv)


eigenvalues, eigenvectors = np.linalg.eig(A)

D = np.diag(eigenvalues)

print("\nMatrix A = V^T B:")
print(A)

print("\nEigenvalues:")
print(np.round(eigenvalues, 6))

print("\nEigenvectors (columns):")
print(np.round(eigenvectors, 6))

print("\nDiagonal matrix D:")
print(np.round(D, 6))
