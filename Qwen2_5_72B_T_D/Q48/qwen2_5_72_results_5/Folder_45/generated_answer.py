def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    present_numbers = set(tup[31:200])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]