def return_binary_or_hexa(arr):
    a = arr[86]
    b = arr[99]
    if a + 1 >= b - 1:
        return ''
    total = sum((i for i in range(a + 1, b) if i not in arr[a + 1:b]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()