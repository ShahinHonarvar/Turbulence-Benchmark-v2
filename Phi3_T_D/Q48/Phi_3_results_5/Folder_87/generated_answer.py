def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[43]
    missing_sum = sum((i for i in range(a + 1, b) if i not in input_tuple[20:43]))
    if missing_sum % 2 == 0:
        return hex(missing_sum).lstrip('0x').upper()
    else:
        return bin(missing_sum).lstrip('0b')