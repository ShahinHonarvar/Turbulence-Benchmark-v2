def return_binary_or_hexa(arr):
    a = arr[56]
    b = arr[90]
    missing_sum = sum(range(a + 1, b)) - sum(set(arr[57:90]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')