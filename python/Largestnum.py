def largest(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num


arr = [4, 8, 2, 10, 6]
print(largest(arr))
