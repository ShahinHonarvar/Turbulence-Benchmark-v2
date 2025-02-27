def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    missing_sum = 0
    present = set(tup[4:9])
    for num in range(a + 1, b):
        if num not in present:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]