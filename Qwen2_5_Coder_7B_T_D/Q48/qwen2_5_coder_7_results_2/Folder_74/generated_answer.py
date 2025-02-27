def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()