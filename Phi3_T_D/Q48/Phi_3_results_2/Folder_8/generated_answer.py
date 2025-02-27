def return_binary_or_hexa(arr):
    a = arr[45]
    b = arr[48]
    if a >= b:
        return ''
    missing_sum = sum([i for i in range(a + 1, b) if i not in arr[45:49]])
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]