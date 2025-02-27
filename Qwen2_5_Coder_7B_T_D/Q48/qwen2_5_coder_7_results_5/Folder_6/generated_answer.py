def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[93]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in tup[a:b + 1]:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()