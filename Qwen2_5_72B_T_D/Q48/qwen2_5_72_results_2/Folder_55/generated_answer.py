def return_binary_or_hexa(data):
    a = data[10]
    b = data[12]
    total_sum = sum(set(range(a + 1, b)) - set(data[11:12]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]