import numpy as np

A = np.array([
    [0.95, 1.00, 1.15, 1.00],
    [2.10, 1.80, 2.21, 2.18],
    [1.00, 2.00, 1.00, 5.00],
    [3.00, 3.10, 3.01, 2.99],
    [0.50, 0.54, 0.48, 0.36],
    [6.00, 5.00, 4.00, 6.00],
    [1.00, 3.00, 1.00, 2.00],
    [0.70, 0.30, 0.36, 0.90]
])


U, S, VT = np.linalg.svd(A, full_matrices=False)

print("Singular Values:")
print(S)

print("\nU matrix:")
print(U)

print("\nV^T matrix:")
print(VT)

# Correlation Coefficient Matrix (between the 4 pictures / columns)
corr_matrix = np.corrcoef(A, rowvar=False)

print("\nCorrelation Coefficient Matrix:")
print(corr_matrix)
