def return_binary_or_hexa(data):
    a = data[80]
    b = data[200]
    present = set(data[81:200])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]