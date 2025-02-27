def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[76]
    total_sum = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in arr[10:77]]
    if missing:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]