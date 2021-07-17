import gdown
import sys

sys.setrecursionlimit(100_000_000)


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def pivot1(arr, l):
    return arr[l]


def pivot2(arr, l, r):
    # pivotを常に先頭に持ってくるためにswapする
    swap(arr, l, r)
    return pivot1(arr, l)


def pivot3(arr, l, r):  # 配列の先頭、真ん中、最後の要素の中央値を返す
    m = l + ((r - l) // 2)

    tmp = [arr[l], arr[m], arr[r]]

    mx = max(tmp)
    mn = min(tmp)

    tmp.remove(mx)
    tmp.remove(mn)

    mid_idx = arr.index(tmp[0])
    swap(arr, l, mid_idx)

    return pivot1(arr, l)


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

    swap(arr, arr.index(p), i-1)

    m = partition(arr, l, i - 2)
    n = partition(arr, i, r)

    return m + n + (r - l)  # 長さmのsubarrayがあるとすると m - 1 = r - l


def main():
    url = 'url of input file'
    output = 'file.txt'
    gdown.download(url, output, quiet=False)

    with open(output) as f:
        numbers = [int(s.strip()) for s in f.readlines()]

    ans = partition(numbers, 0, len(numbers) - 1)
    print(ans)


if __name__ == '__main__':
    main()
