def return_binary_or_hexa(tup):
    a, b = (tup[7], tup[9])
    total_sum = sum(range(a + 1, b)) - sum((int(x) for x in str(a) if x in str(range(a + 1, b)))) - sum((int(x) for x in str(b) if x in str(range(a + 1, b))))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]