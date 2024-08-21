def solution(arr):
    way = 0
    for i in range(len(arr)-1):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                way+=1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(solution([85, 11, 72, 31, 29, 28, 17, 83]))