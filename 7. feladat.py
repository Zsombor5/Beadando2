import numpy as np
def hasonlit(t1, t2):
    sz = 0
    for k in range(len(t1)):
        if t1[k] == t2[k]:
            sz += 1
    if sz == 4:
        return True
    return False
#matrix=np.array([[1,2,1],[2,2,2],[2,2,2],[1,2,3],[2,2,1]])
matrix = np.random.randint(1, 3, (5, 3))
print(matrix)
n = matrix.shape[0] - 1
m = matrix.shape[1] - 1
db = n * m

kettesek = np.zeros((db, 4), dtype=int)
sor = 0
for i in range(n):
    oszlop = 0
    for j in range(m):
        kettesek[sor][oszlop] = matrix[i][j] #0,0
        oszlop += 1
        kettesek[sor][oszlop] = matrix[i][j+1] #0,1
        oszlop += 1
        kettesek[sor][oszlop] = matrix[i+1][j] #1,0
        oszlop += 1
        kettesek[sor][oszlop] = matrix[i+1][j + 1]#1,1
        oszlop = 0
        sor += 1
print(kettesek)
egyformadb = 0
test1 = np.zeros(4)
test2 = np.zeros(4)
for i in range(db-1):
    for j in range(4):
        test1[j] = kettesek[i][j]
    print(test1)

    for i1 in range(i+1, db):
        for j1 in range(4):
            test2[j1] = kettesek[i1][j1]
        if hasonlit(test1, test2):
            egyformadb += 1
print("{} darab különböző 2×2-es mátrixból épül fel.".format(db - egyformadb))
