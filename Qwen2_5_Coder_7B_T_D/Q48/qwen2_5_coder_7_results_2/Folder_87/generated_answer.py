def return_binary_or_hexa(arr):
    a = arr[20]
    b = arr[43]
    total_sum = sum(range(a + 1, b)) - sum((x for x in arr if a < x < b))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]