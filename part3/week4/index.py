c, n = input[0][0], input[0][-1]
A = [[None] * (c+1) for _ in range(n+1)]

for i in range(c+1):
    A[0][i] = 0

for i in range(1, n+1):
    for j in range(c+1):
        v = input[i][0]
        s = input[i][-1]

        if s > j:
            A[i][j] = A[i-1][j]
        else:
            A[i][j] = max(A[i-1][j], (A[i-1][j-s] + v))

print(A[n][c])
