""" leetcode: https://leetcode.com/problems/01-matrix/ solve attempt 1 """

from copy import deepcopy

def check_all_neighbors(mat, row_i, column_i, max_row_i, max_column_i):
    """
    Returns 0 if there is a neighboring zero, returns 1 otherwise
    """

    if row_i != 0:
        if mat[row_i - 1][column_i] == 0:
            return 0

    if row_i != max_row_i:
        if mat[row_i + 1][column_i] == 0:
            return 0

    if column_i != 0:
        if mat[row_i][column_i - 1] == 0:
            return 0

    if column_i != max_column_i:
        if mat[row_i][column_i + 1] == 0:
            return 0

    #neighbor sum will only be zero if all neighbors are 0
    return 1

def update_matrix_1(mat):
    """
    solve attempt 1.
    """
    rows = len(mat)
    columns = len(mat[0])

    loop_check = 1
    #we'll change mat_copy_2 during each round and update mat_cop_1 at the end of each round
    mat_copy_1 = deepcopy(mat)
    mat_copy_2 = deepcopy(mat)

    while loop_check >= 1:
        for i in range(rows):
            for j in range(columns):
                if 1 == check_all_neighbors(mat_copy_1, i, j, (rows -1), (columns - 1)):
                    if mat[i][j] != 0:
                        mat[i][j] += 1
                        mat_copy_2[i][j] += 1

        loop_check = 0

        for i in range(rows):
            for j in range(columns):
                if mat_copy_2[i][j] != 0:
                    mat_copy_2[i][j] -= 1
                    loop_check = 1
                mat_copy_1[i][j] = mat_copy_2[i][j]

    return mat

#End of matrix_sol_2.py file
