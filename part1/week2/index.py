with open(file) as f:
    numbers = [int(s.strip()) for s in f.readlines()]


def count_inversions(arr):
    if len(arr) == 1:
        return 0, arr[:]
    else:
        m = len(arr) // 2

        l = arr[:m]
        r = arr[m:]

        x, l_sorted = count_inversions(l)
        y, r_sorted = count_inversions(r)
        z, sorted = count_split_inversions(l_sorted, r_sorted)

        return x + y + z, sorted


def count_split_inversions(l, r):
    arr = []
    l_car = 0
    r_car = 0
    cnt = 0

    while l_car < len(l) and r_car < len(r):
        if l[l_car] <= r[r_car]:
            arr.append(l[l_car])
            l_car += 1
        else:
            arr.append(r[r_car])
            r_car += 1
            cnt += len(l) - l_car

    arr.extend(l[l_car:])
    arr.extend(r[r_car:])

    return cnt, arr


ans = count_inversions(numbers)
print(ans)
