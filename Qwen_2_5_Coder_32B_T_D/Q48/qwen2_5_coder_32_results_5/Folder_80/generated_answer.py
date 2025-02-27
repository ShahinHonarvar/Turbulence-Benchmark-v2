def return_binary_or_hexa(tup):
    a, b = (tup[57], tup[84])
    total_sum = 0
    seen = set(tup[57:85])
    for num in range(a + 1, b):
        if num not in seen:
            total_sum += num
    if total_sum % 2:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''