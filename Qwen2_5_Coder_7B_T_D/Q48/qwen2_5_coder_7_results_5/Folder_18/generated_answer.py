def return_binary_or_hexa(num_tuple):
    a = num_tuple[56]
    b = num_tuple[90]
    total_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[a + 1:b]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()