""" leetcode: https://leetcode.com/problems/01-matrix/ solve attempt 2 """

from copy import deepcopy
from collections import deque

def update_matrix_2(mat):
    """
    Solve the matrix problem.
    """
    m, n = len(mat), len(mat[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    distance = deepcopy(mat)

    for x_index in range(m):
        for y_index in range(n):
            distance[x_index][y_index] = float('inf') * mat[x_index][y_index]

    queue = deque()

    for x_index in range(m):
        for y_index in range(n):
            if mat[x_index][y_index] == 0:
                queue.append((x_index, y_index))
                distance[x_index][y_index] = 0

    while queue:
        x_index, y_index = queue.popleft()
        for x_change, y_change in directions:
            x_check, y_check = x_index + x_change, y_index + y_change
            if 0 <= x_check < m and 0 <= y_check < n:
                if distance[x_check][y_check] > distance[x_index][y_index]:
                    queue.append((x_check, y_check))
                    distance[x_check][y_check] = distance[x_index][y_index] + 1

    return distance

#End of matrix_sol_2.py file
