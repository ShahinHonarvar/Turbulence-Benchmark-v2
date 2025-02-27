def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[8]
    total_sum = 0
    num_set = set(tup[:9])
    for num in range(a + 1, b):
        if num not in num_set:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]