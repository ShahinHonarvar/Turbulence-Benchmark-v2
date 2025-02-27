def return_binary_or_hexa(arr):
    a = arr[57]
    b = arr[85]
    total = 0
    for i in range(a + 1, b):
        if i not in arr:
            total += i
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]