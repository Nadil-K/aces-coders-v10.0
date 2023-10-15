# Cube Nets

def is_valid_net(squares):
    if len(squares) != 6:
        return False
    # Further validation can be done here
    return True

def explore_net(matrix, i, j, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] != '#':
        return []
    visited[i][j] = True
    squares = [(i, j)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    for di, dj in directions:
        squares += explore_net(matrix, i + di, j + dj, visited)
    return squares

def count_nets(matrix):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    valid_nets = 0
    invalid_nets = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j] and matrix[i][j] == '#':
                net_squares = explore_net(matrix, i, j, visited)
                if is_valid_net(net_squares):
                    valid_nets += 1
                else:
                    invalid_nets += 1
    return valid_nets, invalid_nets

n = int(input())

for i in range(n):
    m, n = map(int, input().split())
    matrix = [list(input()) for _ in range(m)]
    valid_nets, invalid_nets = count_nets(matrix)
    print(f'{valid_nets} {invalid_nets}')

