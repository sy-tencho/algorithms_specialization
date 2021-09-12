n = input[0]
weights = [-1 for _ in range(n + 1)]
for i in range(1, n + 1):
    weights[i] = input[i]


A = [0 for _ in range(n + 1)]
A[0] = 0
A[1] = weights[1]

for i in range(2, n + 1):
    A[i] = max(A[i - 1], (A[i - 2] + weights[i]))


S = []
j = n
while j >= 2:
    if A[j - 1] >= A[j - 2] + weights[j]:
        j = j - 1
    else:
        S.append(j)
        j = j - 2


if j == 1:
    S.append(j)


ans = ''
nodes = [1, 2, 3, 4, 17, 117, 517, 997]
for node in nodes:
    if node in S:
        ans += '1'
    else:
        ans += '0'

print(ans)
