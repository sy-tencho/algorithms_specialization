# Runs on Google Colab

import gdown
import bisect

url = 'url to file'
input = 'file.txt'
gdown.download(url, input, quiet=False)

f = open('file.txt', 'r')
N = sorted((int(l) for l in f.readlines()))


def two_sum(numbers):
    sum_list = {}
    t = 10_000

    for x in numbers:
        mn = bisect.bisect_left(numbers, -x - t)
        mx = bisect.bisect_left(numbers, t - x)

        tmp = numbers[mn:mx]

        if x in tmp:
            tmp.remove(x)

        for n in tmp:
            sum_list[x+n] = True

    return len(sum_list.keys())
