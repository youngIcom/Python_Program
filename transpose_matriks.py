def transpose_manual(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


#penggunaan
matrix_awal = [[1,2,3],
               [4,5,6]]

matrix_transpose = transpose_manual(matrix_awal)
print("matrix awal ")
for row in matrix_awal:
    print(row)

print("\nMatriks transpose manual : ")
for row in matrix_transpose:
    print(row)
