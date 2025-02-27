def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[52]
    present = set(tup[36:53])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]