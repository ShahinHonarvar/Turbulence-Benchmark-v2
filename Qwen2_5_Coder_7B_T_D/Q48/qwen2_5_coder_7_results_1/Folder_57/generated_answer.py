def return_binary_or_hexa(arr):
    a = arr[25]
    b = arr[80]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in arr[a + 1:b]:
            total_sum += i
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')