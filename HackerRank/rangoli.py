import string

def print_rangoli(size):
    # result = []
    # result_ = []
    # for i in string.ascii_lowercase[:size]:
    #     result.append(i)
    # value = '-'.join(result) 
    # value_ = value[::-1] + value[1:]
    # for i in value_[:int(len(value_)/2)+1]:
    #     if i.isalpha():
    #         nilai = value_[:value_.index(i)]
    #         print(nilai + ''.join(list(reversed(nilai))))
    alpha = string.ascii_lowercase[:size+1]
    result = []
    for i in range(1, len(alpha)):
        result.append(alpha[:i])
    for i in result:
        print(i.center(len(alpha), '-'))
    
print(print_rangoli(5))