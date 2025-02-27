def return_binary_or_hexa(values):
    a = values[10]
    b = values[76]
    missing_sum = sum((i for i in range(a + 1, b) if i not in values[10:77]))
    return bin(missing_sum)[2:] if missing_sum % 2 else f'{missing_sum:x}'