import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    
    r=len(A)
    c=len(A[0])
    result=np.empty((c,r),dtype=np.array(A).dtype)
    for i in range(r):
        for j in range(c):
            result[j][i]=A[i][j]
    return result