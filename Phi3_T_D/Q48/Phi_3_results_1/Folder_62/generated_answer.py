def return_binary_or_hexa(tup):
    a, b = (tup[50], tup[92])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[50:92]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]