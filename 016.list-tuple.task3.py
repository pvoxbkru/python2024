mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

diag1 = list()
# diag1.append(mtx[0][0])
# diag1.append(mtx[1][1])
# diag1.append(mtx[2][2])
[diag1.append(mtx[x][x]) for x in range(3)]
print(diag1)

diag2 = list()
# diag2.append(mtx[0][2])
# diag2.append(mtx[1][1])
# diag2.append(mtx[2][0])
[diag2.append(mtx[x][y]) for x, y in zip(range(3), range(2, -1, -1))]
print(diag2)
