def binary_search(arr, target):
    min = 0
    max = len(arr) -1
    guess = int((min+max)/2)
    while arr[guess]!=target:
        if arr[guess]< target:
            min+=1
            guess = int((min+max)/2)
        elif arr[guess] > target:
            max = guess
            guess =int((min+max)/2)
    else:
        return guess
    

print(binary_search([2, 3, 5, 7, 9, 11, 13, 17, 23], 23))