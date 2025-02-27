def return_binary_or_hexa(num_tuple):
    a = num_tuple[90]
    b = num_tuple[200]
    missing_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[90:200]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].capitalize()
    else:
        return bin(missing_sum)[2:]