import gdown
import sys

url = 'url'
file_name = 'file.txt'
gdown.download(url, input, quiet=False)

f = open(file_name, 'r')
input = [l.split() for l in f.readlines()]

# difference
numbers = []

for n in input[1:]:
    w, l = int(n[0]), int(n[1])
    d = w - l

    numbers.append([w, l, d])

# ratio
numbers2 = []

for n in input[1:]:
    w, l = int(n[0]), int(n[1])
    r = w / l

    numbers2.append([w, l, r])


def min_weighted_sum(nums):
    len_sum = 0
    ans = 0

    for num in nums:
        len_sum = len_sum + num[1]
        ans += len_sum * num[0]

    return ans
