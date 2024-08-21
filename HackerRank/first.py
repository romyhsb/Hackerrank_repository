# import math
# def solution(string_, width):
#     result = []
#     indeks = 0
#     new_width = width
#     for i in range(math.ceil((len(string_)/width))):
#         result.append(string_[indeks:width])
#         indeks=width
#         width = width+new_width 
#     return '\n'.join(result)


# print(solution('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))

thickness=5
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)) 

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))