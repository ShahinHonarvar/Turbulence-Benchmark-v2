def return_binary_or_hexa(integers):
    a = integers[11]
    b = integers[76]
    missing_sum = sum(set(range(a + 1, b)) - set(integers[11:77]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]