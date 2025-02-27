def return_binary_or_hexa(data):
    if len(data) < 89 or data[17] >= data[88]:
        return ''
    missing_sum = sum(set(range(data[17] + 1, data[88])) - set(data[18:88]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]