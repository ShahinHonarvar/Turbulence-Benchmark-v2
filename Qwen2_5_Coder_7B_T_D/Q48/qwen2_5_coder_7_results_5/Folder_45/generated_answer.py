def return_binary_or_hexa(arr):
    a = arr[30]
    b = arr[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(arr[30:201])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]