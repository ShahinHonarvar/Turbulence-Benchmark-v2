def return_binary_or_hexa(data):
    a = data[13]
    b = data[76]
    subset = set(data[13:77])
    total_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]