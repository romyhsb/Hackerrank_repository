# def count_substring(string, sub_string):
#     resutl = []
#     index = len(sub_string)
#     for i in range(0, len(string)):
#         resutl.append(string[i:index])
#         index+=1
#     return len([i for i in resutl if i==sub_string])


# print(count_substring('ABCDCDC', 'CDC'))

     
def check_upper(s):
    if s.isalnum():
        for i in s:
            if i.isupper():
                print(True)
                break
            
print(check_upper('au'))