def return_binary_or_hexa(arr):
    a, b = (arr[48], arr[76])
    missing_sum = sum((i for i in range(a + 1, b) if i not in arr[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()