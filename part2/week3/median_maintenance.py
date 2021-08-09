# Runs on Google Colab
import gdown

url = 'url to file'
input = 'file.txt'
gdown.download(url, input, quiet=False)

f = open('file.txt', 'r')
F = [int(l) for l in f.readlines()]

ans = median_maintenance(F)
print(sum(ans) % 10_000)


def heap_min_push(q, x):
    if q == []:
        q.append(None)

    q.append(x)
    return bubble_up_min(q, len(q) - 1)


def bubble_up_min(q, i):
    p_idx = i // 2

    c = q[i]
    p = q[p_idx]

    if i == 1 or c > p:
        return q

    q[i], q[p_idx] = q[p_idx], q[i]
    return bubble_up_min(q, p_idx)


def heap_min_pop(q):
    tail_idx = len(q) - 1
    mn = q[1]

    q[1], q[tail_idx] = q[tail_idx], q[1]
    q.pop(tail_idx)

    heapified = bubble_down_min(q, 1)

    return mn, heapified


def bubble_down_min(q, i):
    tail_idx = len(q) - 1
    l_idx, r_idx = i * 2, i * 2 + 1

    l, r = None, None

    if l_idx <= tail_idx:
        l = q[l_idx]
    if r_idx <= tail_idx:
        r = q[r_idx]

    if l is None:
        # childがいないバターン
        return q
    else:
        if r is None:
            # left childだけいるパターン
            if q[i] > l:
                q[i], q[l_idx] = q[l_idx], q[i]
            return q
        else:
            # childが両方いるパターン
            mn = min(q[i], l, r)
            if mn == q[i]:
                return q
            elif mn == l:
                q[i], q[l_idx] = q[l_idx], q[i]
                bubble_down_min(q, l_idx)
            elif mn == r:
                q[i], q[r_idx] = q[r_idx], q[i]
                bubble_down_min(q, r_idx)

    return q


def heap_max_push(q, x):
    if q == []:
        q.append(None)

    q.append(x)
    return bubble_up_max(q, len(q) - 1)


def bubble_up_max(q, i):
    p_idx = i // 2

    c = q[i]
    p = q[p_idx]

    if i == 1 or c < p:
        return q

    q[i], q[p_idx] = q[p_idx], q[i]
    return bubble_up_max(q, p_idx)


def heap_max_pop(q):
    tail_idx = len(q) - 1
    mx = q[1]

    q[1], q[tail_idx] = q[tail_idx], q[1]
    q.pop(tail_idx)

    heapified = bubble_down_max(q, 1)

    return mx, heapified


def bubble_down_max(q, i):
    tail_idx = len(q) - 1
    l_idx, r_idx = i * 2, i * 2 + 1

    l, r = None, None

    if l_idx <= tail_idx:
        l = q[l_idx]
    if r_idx <= tail_idx:
        r = q[r_idx]

    if l is None:
        # childがいないバターン
        return q
    else:
        if r is None:
            # left childだけいるパターン
            if q[i] < l:
                q[i], q[l_idx] = q[l_idx], q[i]
            return q
        else:
            # childが両方いるパターン
            mx = max(q[i], l, r)
            if mx == q[i]:
                return q
            elif mx == l:
                q[i], q[l_idx] = q[l_idx], q[i]
                bubble_down_max(q, l_idx)
            elif mx == r:
                q[i], q[r_idx] = q[r_idx], q[i]
                bubble_down_max(q, r_idx)

    return q


def median_maintenance(numbers):
    L, R = [], []
    ans = []

    for i, x in enumerate(numbers):
        if i == 0:
            heap_max_push(L, x)
            ans.append(x)
            continue
        if i == 1:
            first_element, _ = heap_max_pop(L)
            mn = min(first_element, x)
            mx = max(first_element, x)
            ans.append(mn)

            heap_max_push(L, mn)
            heap_min_push(R, mx)

            continue

        pointer = i + 1
        is_pointer_even = pointer % 2 == 0

        l, _ = heap_max_pop(L)
        r, _ = heap_min_pop(R)

        tmp = [l, r, x]
        tmp.sort()

        L = heap_max_push(L, tmp[0])
        R = heap_min_push(R, tmp[-1])

        if is_pointer_even:
            R = heap_min_push(R, tmp[1])
        else:
            L = heap_max_push(L, tmp[1])

        ans.append(L[1])

    return ans
