def return_binary_or_hexa(arr):
    a = arr[34]
    b = arr[69]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in arr[34:69 + 1]:
            missing_sum += i
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')