# def solution(n):
#     odd_number = []
#     odd = 1
#     sub = []
#     while len(odd_number)!=n:
#         for i in range(1, n+1):
#             for x in range(1, i+1):
#                 sub.append(odd)
#                 odd+=2
#             odd_number.append(sub)
#             sub = sub[:0]
#     return sum([i for i in odd_number[-1]])


# print(solution(7))


# """
# algorithma 
# 1. buat list yang menampung bilangan ganjil per range of n 
#     a. buat looping untuk setiap tingkatan angka 
#     b. while len(odd number) != n

# 2.  
# """

a = ':~D'

import re
pattern = r'[:;][-~]*[)D]'
if re.fullmatch(pattern, a):
    print(True)