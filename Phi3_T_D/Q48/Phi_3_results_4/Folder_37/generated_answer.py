def return_binary_or_hexa(input_tuple):
    a = input_tuple[2]
    b = input_tuple[7]
    missing_sum = sum(set(range(a + 1, b)) - set(input_tuple[2:7]))
    if missing_sum % 2 == 0:
        return hex(missing_sum).lstrip('0x').upper()
    else:
        return bin(missing_sum)[2:]