# def permutasion(s, n):
#     first = [i for i in range(1, s+1)]
#     index = 1
#     for i in first:
#         index*=i
#     second = [i for i in range(1, int(s-n)+1)]
#     index_ = 1
#     for i in second:
#         index_*=i
#     return int(index/index_)

# def solution(string, m):
#     result = []
#     barier = permutasion(len(string), m)
#     for k in range(barier):
#             for i in string:
#                 for j in string[::-1]:
#                     if [i, j] not in result and i !=j:
#                         result.append([i, j])  
#     real = ''                
#     for i, j in sorted(result):
#          print(i+j)         

# print(solution("XYZ", 1))


# def printme(str):

#    "This prints a passed string into this function"

#    print (str)

#    return

# printme("hello world")
# i = 12
# indeks = 0
# while indeks!=i:
#     result = (indeks*i)/9
#     if type(result)==float:
#         print(indeks+7)
#         indeks+=1
#     else:
#         indeks+=1

def sorting(arr):
   urut = sorted(arr)
   result = []
   
   while arr!=urut:
      way = 0
      indeks = 0
      if arr[indeks]!=urut[indeks]:
         minimum = arr.index(min(arr))
         arr[indeks], arr[minimum] = arr[minimum], arr[indeks]
         way+=1
      else:
         continue
      indeks+=1
   return way


   # while result!=urut: 
   #    way = 0
   #    indeks = 0
   #    for i in arr:
   #       if urut[indeks]!=arr[indeks]:
   #          minu = min(arr)
   #          result.append(minu)
   #          arr.remove(minu)
   #          way+=1
   #       else:
   #          result.append(i)
   #    indeks+=1
   return way
      
print(sorting([7, 2, 9, 1, 4]))