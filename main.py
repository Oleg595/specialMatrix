import sympy as sp
# Критерий Баумана
def printMatrix(A):
    exp = [sp.det(A) < 0]
    print("A =", A, "|A| = ", sp.det(A), )
    print(exp, ":", sp.solve(exp, (e)))
    exp = [sp.det(A) > 0]
    print(exp, ":", sp.solve(exp, (e)))
    print()

e = sp.symbols('e', real=True, nonnegative=True)
printMatrix(sp.Matrix([[1 - e, 1.1 - e], [1 - e, 1 - e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 - e], [1 - e, 1 + e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 - e], [1 + e, 1 - e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 - e], [1 + e, 1 + e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 + e], [1 - e, 1 - e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 + e], [1 - e, 1 + e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 + e], [1 + e, 1 - e]]))
printMatrix(sp.Matrix([[1 - e, 1.1 + e], [1 + e, 1 + e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 - e], [1 - e, 1 - e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 - e], [1 - e, 1 + e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 - e], [1 + e, 1 - e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 - e], [1 + e, 1 + e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 + e], [1 - e, 1 - e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 + e], [1 - e, 1 + e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 + e], [1 + e, 1 - e]]))
printMatrix(sp.Matrix([[1 + e, 1.1 + e], [1 + e, 1 + e]]))

print()

printMatrix(sp.Matrix([[1 - e, 1.1 - e], [1, 1]]))
printMatrix(sp.Matrix([[1 - e, 1.1 + e], [1, 1]]))
printMatrix(sp.Matrix([[1 + e, 1.1 - e], [1, 1]]))
printMatrix(sp.Matrix([[1 + e, 1.1 + e], [1, 1]]))

print()

# Критерий Румпа
def matrixSingularNumbers(matrix):
    r = sp.Matrix(matrix * sp.Transpose(matrix)).eigenvals()
    print("A:", matrix)
    print("A^t * A:", matrix * sp.Transpose(matrix))
    print("|A^t * A|:", r)
    print()
    result = []
    for i in list(r):
        result.append(i)
    return result

matrixSingularNumbers(sp.Matrix([[1, 1.1], [1, 1]]))
matrixSingularNumbers(sp.Matrix([[e, e], [0, 0]]))

print()

nums = matrixSingularNumbers(sp.Matrix([[1, 1.1], [1, 1]]))
exprs = matrixSingularNumbers(sp.Matrix([[e, e], [e, e]]))

print(min(nums))
print(exprs)

print("Крайние матрицы полиномиальной регрессии:")

print("x = [0.9 - e, 0.9 + e]")
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 - e) ** 2, (0.9 - e) ** 2], [1 - e, 1.1 - e, 0.9 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 - e) ** 2, (0.9 + e) ** 2], [1 - e, 1.1 - e, 0.9 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 + e) ** 2, (0.9 - e) ** 2], [1 - e, 1.1 + e, 0.9 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 + e) ** 2, (0.9 + e) ** 2], [1 - e, 1.1 + e, 0.9 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 - e) ** 2, (0.9 - e) ** 2], [1 + e, 1.1 - e, 0.9 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 - e) ** 2, (0.9 + e) ** 2], [1 + e, 1.1 - e, 0.9 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 + e) ** 2, (0.9 - e) ** 2], [1 + e, 1.1 + e, 0.9 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 + e) ** 2, (0.9 + e) ** 2], [1 + e, 1.1 + e, 0.9 + e], [1, 1, 1]]))

print("x = [0.95 - e, 0.95 + e]")
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 - e) ** 2, (0.95 - e) ** 2], [1 - e, 1.1 - e, 0.95 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 - e) ** 2, (0.95 + e) ** 2], [1 - e, 1.1 - e, 0.95 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 + e) ** 2, (0.95 - e) ** 2], [1 - e, 1.1 + e, 0.95 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 - e) ** 2, (1.1 + e) ** 2, (0.95 + e) ** 2], [1 - e, 1.1 + e, 0.95 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 - e) ** 2, (0.95 - e) ** 2], [1 + e, 1.1 - e, 0.95 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 - e) ** 2, (0.95 + e) ** 2], [1 + e, 1.1 - e, 0.95 + e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 + e) ** 2, (0.95 - e) ** 2], [1 + e, 1.1 + e, 0.95 - e], [1, 1, 1]]))
printMatrix(sp.Matrix([[(1 + e) ** 2, (1.1 + e) ** 2, (0.95 + e) ** 2], [1 + e, 1.1 + e, 0.95 + e], [1, 1, 1]]))
