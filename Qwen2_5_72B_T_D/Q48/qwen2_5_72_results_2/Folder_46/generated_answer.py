def return_binary_or_hexa(data):
    a = data[10]
    b = data[79]
    present = set(data[10:80])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]