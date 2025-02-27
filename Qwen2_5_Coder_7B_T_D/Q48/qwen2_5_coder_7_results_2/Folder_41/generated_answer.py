def return_binary_or_hexa(arr):
    a = arr[3]
    b = arr[8]
    total_sum = sum(range(a + 1, b))
    missing_ints = [i for i in range(a + 1, b) if i not in arr[3:8]]
    if missing_ints:
        total_sum = sum(missing_ints)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()