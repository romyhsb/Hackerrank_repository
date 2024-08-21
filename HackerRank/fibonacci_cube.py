# a = [2, 3, 5]
# cube = lambda x : x**3

# print(list(map(cube, a)))

def fibonacci(n):
    result = [0, 1]
    first_indeks = 0
    second_indeks = 1
    if n >1:
        for i in range(n-2):
            value = result[first_indeks]+result[second_indeks]
            result.append(value)
            first_indeks+=1
            second_indeks+=1
        return result
    elif n ==1:
        return [result[0]]
    else:
        return []

print(fibonacci(0))