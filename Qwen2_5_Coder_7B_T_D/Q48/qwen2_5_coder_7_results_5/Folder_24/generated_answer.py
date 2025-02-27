def return_binary_or_hexa(arr):
    a = arr[13]
    b = arr[91]
    total = 0
    for i in range(a + 1, b):
        if i not in arr[a + 1:b]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()