def return_binary_or_hexa(arr):
    a = arr[275]
    b = arr[871]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(arr[275:872])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()