import random
import unittest
import Lab2


class Test(unittest.TestCase):
    def test_multiply_matrix_and_matrix(self):
        mat1 = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
        mat2 = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
        self.assertEqual(Lab2.multiplyMatrixAndMatrix(mat1, mat2), Lab2.multiplyWithNumpy(mat1, mat2))

    def test_multiply_matrix_and_vector(self):
        mat = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
        vec = [random.randint(0, 1) for _ in range(100)]
        self.assertEqual(Lab2.multiplyMatrixAndVector(mat, vec), Lab2.multiplyWithNumpy(mat, vec))

    def test_multiply_vector_and_matrix(self):
        vec = [random.randint(0, 1) for _ in range(100)]
        mat = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]
        self.assertEqual(Lab2.multiplyVectorAndMatrix(vec, mat), Lab2.multiplyWithNumpy(vec, mat))

    def test_multiply_vector_and_vector(self):
        vec1 = [random.randint(0, 1) for _ in range(100)]
        vec2 = [random.randint(0, 1) for _ in range(100)]
        self.assertEqual(Lab2.multiplyVectorAndVector(vec1, vec2), Lab2.multiplyWithNumpy(vec1, vec2))


if __name__ == '__main__':
    unittest.main()
