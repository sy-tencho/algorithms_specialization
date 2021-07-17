import gdown
import sys

url = ''
output = 'file.txt'
gdown.download(url, output, quiet=False)

with open(output) as f:
    numbers = [int(s.strip()) for s in f.readlines()]

sys.setrecursionlimit(100_000_000)


def partition(arr, l, r):  # l, r: 各ルーティン内の探索範囲
    if l >= r:
        return 0

    # p = pivot1(arr, l)
    # p = pivot2(arr, l, r)
    p = pivot3(arr, l, r)

    i = l + 1

    for j in range(l+1, r+1):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[arr.index(p)], arr[i-1] = arr[i-1], arr[l]

    m = partition(arr, l, i - 2)
    n = partition(arr, i, r)

    return m + n + (r - l)  # 長さmのsubarrayがあるとすると r - l = m - 1


def pivot1(arr, l):
    return arr[l]


def pivot2(arr, l, r):
    # pivotを常に先頭に持ってくるためにswapする
    arr[l], arr[r] = arr[r], arr[l]
    return pivot1(arr, l)


def pivot3(arr, l, r):
    m = l + ((r - l) // 2)

    tmp = [arr[l], arr[m], arr[r]]

    mx = max(tmp)
    mn = min(tmp)

    tmp.remove(mx)
    tmp.remove(mn)

    mid_idx = arr.index(tmp[0])
    arr[l], arr[mid_idx] = arr[mid_idx], arr[l]

    return pivot1(arr, l)
