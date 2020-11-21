# from itertools import accumulate
#
#
# n = int(input())
# worms = list((map(int, input().split())))
# m = int(input())
# succulent_worms = list(map(int, input().split()))
# end_indices = list(accumulate(worms))
# intervals = []
# begin = 1
# for i in range(n):
#     end = end_indices[i]
#     intervals.append([begin, end])
#     begin = end + 1
# for i in range(m):
#     for j in range(len(intervals)):
#         left = intervals[j][0]
#         right = intervals[j][1]
#         if succulent_worms[i] in range(left, right + 1):
#             print(j + 1)

from bisect import bisect_left


n = int(input())
worms = list(map(int, input().split()))
m = int(input())
end_indices = [worms[0]]
for j in worms[1:]:
    end_indices.append(end_indices[-1] + j)
succulent_worms = list(map(int, input().split()))
for j in succulent_worms:
    print(bisect_left(end_indices, j) + 1)
