def return_binary_or_hexa(data):
    a = data[86]
    b = data[99]
    present = set(data[86:100])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    if missing_sum == 0:
        return ''
    return hex(missing_sum)[2:]