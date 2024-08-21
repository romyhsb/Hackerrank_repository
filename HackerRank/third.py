# x = 1
# y = 1
# z = 2
# n = 3

a  = 0
result = []
def solution(x, y, z, n):
    # x = list(range(0, x+1))
    # y = list(range(0, y+1))
    # z = list(range(0, z+1))
    result = []
    for h in range(0, x+1):
        for i in range(0, y+1):
            for j in range(0, z+1):
                if [h, i, j] not in result:
                    result.append([h, i, j])

    return [i for i in result if sum(i)!=n]
print(solution(1, 1, 2, 3))