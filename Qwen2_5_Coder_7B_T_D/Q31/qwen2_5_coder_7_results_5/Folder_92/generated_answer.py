def if_perfect_num(arr):
    return arr[0] == sum([i for i in range(1, arr[0]) if arr[0] % i == 0])