def return_binary_or_hexa(arr):
    a = arr[57]
    b = arr[85]
    missing_sum = sum(range(a + 1, b)) - sum((arr[i] for i in range(57, 86)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()