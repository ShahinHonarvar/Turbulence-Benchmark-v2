def return_binary_or_hexa(numbers_tuple):
    present = set(numbers_tuple[62:97])
    a, b = (numbers_tuple[62], numbers_tuple[96])
    if b <= a:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 0:
        hexa_repr = hex(missing_sum)[2:].upper()
        return hexa_repr
    else:
        binary_repr = bin(missing_sum)[2:]
        return binary_repr