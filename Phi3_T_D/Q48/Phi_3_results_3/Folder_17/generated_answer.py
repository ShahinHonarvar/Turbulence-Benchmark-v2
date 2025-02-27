def return_binary_or_hexa(integers):
    a = integers[73]
    b = integers[84]
    missing_sum = sum(range(a + 1, b)) - sum(integers[73:85])
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()