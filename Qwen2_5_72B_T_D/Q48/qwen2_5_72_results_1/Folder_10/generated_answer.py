def return_binary_or_hexa(tup):
    if len(tup) < 55:
        return ''
    a = tup[36]
    b = tup[54]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in tup:
            missing_sum += i
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]