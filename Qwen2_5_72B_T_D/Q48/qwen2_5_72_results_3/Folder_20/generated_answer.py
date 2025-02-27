def return_binary_or_hexa(data):
    a = data[27]
    b = data[96]
    present = set(data[27:97])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]