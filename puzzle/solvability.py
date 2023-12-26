def is_solvable(matrix) -> bool:
    inversion_count = 0
    row_major_order = [value for row in matrix for value in row if value != 0]

    for i in range(8):
        for j in range(i + 1, 8):
            if row_major_order[i] > row_major_order[j]:
                inversion_count += 1

    return inversion_count % 2 == 0
