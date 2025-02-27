def return_binary_or_hexa(int_tuple):
    a = int_tuple[44]
    b = int_tuple[91]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in int_tuple[44:92]:
            missing_sum += i
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return bin(missing_sum)[2:]