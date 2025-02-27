def return_binary_or_hexa(tuple):
    sum = sum((i for i in range(tuple[10] + 1, tuple[76]) if i not in tuple[10:77]))
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:]