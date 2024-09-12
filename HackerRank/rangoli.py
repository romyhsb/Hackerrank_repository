import string
def rangoli(size):
    alpha = string.ascii_lowercase[:size]
    value = '-'.join(list(alpha))
    real_value =  value[::-1] + value[1:]
    result = []
    indeks = 6
    for i in range(size):
        char = real_value[:indeks]
        yeah = char + char[-2::-1]
        result.append(yeah.center(len(real_value), '-'))
        indeks+=2
    return '\n'.join(result) + '\n' + '\n'.join(result[-2::-1])
rangoli(5)
