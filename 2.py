
def count_islands(map):

    if not map:
        return 0

    m, n = len(map), len(map[0])
    visited = set()

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and (i, j) not in visited and map[i][j] == 1:
            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

    num_islands = 0

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and map[i][j] == 1:
                dfs(i, j)
                num_islands += 1
    return num_islands

map1 = [[0, 1, 0], [0, 0, 0], [0, 1, 1]]
print(count_islands(map1))

map2 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
print(count_islands(map2))

map3 = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]]
print(count_islands(map3))