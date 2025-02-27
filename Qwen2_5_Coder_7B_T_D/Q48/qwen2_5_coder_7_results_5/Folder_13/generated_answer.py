def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    total_sum = sum(range(a + 1, b))
    included_sum = sum((tup[i] for i in range(46, 92)))
    result_sum = total_sum - included_sum
    if result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:].upper()