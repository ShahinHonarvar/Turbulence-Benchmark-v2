def return_binary_or_hexa(int_tuple):
    a = int_tuple[10] if len(int_tuple) > 10 else float('inf')
    b = int_tuple[76] if len(int_tuple) > 76 else float('inf')
    missing_sum = sum(set(range(a + 1, b)) - set(int_tuple[10:77]))
    if missing_sum == 0:
        return ''
    else:
        representation = hex(missing_sum) if missing_sum % 2 == 0 else bin(missing_sum)[2:]
        return representation.upper() if representation.isdigit() else representation