def square_matrix_map(matrix=[]):
    return list(map(lambda n: list(map(lambda op: op * op, n)), matrix))
    