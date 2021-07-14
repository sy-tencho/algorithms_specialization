# calculate the expectation of sum of 2 dices

l = [1, 2, 3, 4, 5, 6]

# Brute force
h = {}

for i in l:
    for j in l:
        sm = i + j

        if str(sm) in h:
            h[sm] += 1
        else:
            h[sm] = 1

s, p = 0, 0

for k in h.keys():
    p += h[k]
    s += int(k) * h[k]

exp = s // p

print(exp)

# E[Σn(i=1 to i=n)Xj] = Σn(i=1 to i=n)E[Xj]
exp2 = (sum(l) / len(l)) * 2
print(exp2)
