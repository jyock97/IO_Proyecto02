
mat = []
res = []
n = 0
m = 0

def dSolve(i, j):
    global mat, res, n, m

    if (i < 0 or i >= n):
        return -1

    if (j == m-1):
        res[i][j] = mat[i][j]
        return res[i][j]

    res[i][j] = mat[i][j] + max(dSolve(i-1, j+1),
                                dSolve(i, j+1),
                                dSolve(i+1, j+1))
    return res[i][j]

def main():
    global mat, res, n, m
    maxNum = 0

    with open("mina.txt") as f:

        i = 0
        for line in f:
            line = line.rstrip("\n")
            mat.append([])
            res.append([])
            for num in line.split(", "):
                mat[i].append(int(num))
                res[i].append(0)
            i+=1

    n = len(mat)
    m = len(mat[0])

    for i in range(0, n):
        maxNum = max(maxNum, dSolve(i, 0))

    print(mat)
    print(res)
    print(maxNum)

if __name__ == '__main__':
    main()
