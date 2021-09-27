import random
import numpy as np
import time

def multiplyMatrixAndMatrix(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def multiplyMatrixAndVector(mat, vec):
    result = [0 for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i] += mat[i][j] * vec[j]
    return result


def multiplyVectorAndMatrix(vec, mat):
    result = [0 for i in range(len(vec))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i] += mat[j][i] * vec[j]
    return result


def multiplyVectorAndVector(vec1, vec2):
    result = 0
    for i in range(len(vec1)):
        result += vec1[i]*vec2[i]
    return result


def multiplyWithNumpy(arr1, arr2):
    return np.dot(arr1, arr2).tolist()

mat1 = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
mat2 = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
vec1 = [random.randint(0, 1) for _ in range(100)]
vec2 = [random.randint(0, 1) for _ in range(100)]

print('*'*100)
print('Множення двох матриць')
startTime = time.time()
multiplyMatrixAndMatrix(mat1, mat2)
endTime = time.time()
print(f'Час без використання Numpy {endTime-startTime} cекунд')
startTime = time.time()
multiplyWithNumpy(mat1, mat2)
endTime = time.time()
print(f'Час з використання Numpy {endTime-startTime} cекунд')
print('*'*100)
print('Множення матриці на вектор')
startTime = time.time()
multiplyMatrixAndVector(mat1, vec1)
endTime = time.time()
print(f'Час без використання Numpy {endTime-startTime} cекунд')
startTime = time.time()
multiplyWithNumpy(mat1, vec1)
endTime = time.time()
print(f'Час з використання Numpy {endTime-startTime} cекунд')
print('*'*100)
print('Множення вектора на матрицю')
startTime = time.time()
multiplyVectorAndMatrix(vec1, mat1)
endTime = time.time()
print(f'Час без використання Numpy {endTime-startTime} cекунд')
startTime = time.time()
multiplyWithNumpy(vec1, mat1)
endTime = time.time()
print(f'Час з використання Numpy {endTime-startTime} cекунд')
print('*'*100)
print('Множення двох векторів')
startTime = time.time()
multiplyVectorAndVector(vec1, vec2)
endTime = time.time()
print(f'Час без використання Numpy {endTime-startTime} cекунд')
startTime = time.time()
multiplyWithNumpy(vec1, vec2)
endTime = time.time()
print(f'Час з використання Numpy {endTime-startTime} cекунд')
