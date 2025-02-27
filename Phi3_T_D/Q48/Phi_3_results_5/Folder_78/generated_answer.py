def return_binary_or_hexa(number_tuple):
    a = number_tuple[62]
    b = number_tuple[96]
    missing_sum = sum((y for y in range(a + 1, b) if y not in number_tuple[62:97]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]