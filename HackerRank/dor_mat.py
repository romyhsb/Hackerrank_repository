def solution(n, m):
    middle_ = 1
    char = '.|.'
    welcome = 'WELCOME'
    result = []
    for i in range(int(n/2)):
        line = char*middle_
        result.append(line.center(m, '-'))
        middle_+=2

    return '\n'.join(result) + '\n'+ welcome.center(m, '-') +'\n' + '\n'.join(result[::-1])

print(solution(11, 33))
