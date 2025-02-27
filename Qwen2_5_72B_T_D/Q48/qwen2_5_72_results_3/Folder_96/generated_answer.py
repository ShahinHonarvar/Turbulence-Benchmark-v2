def return_binary_or_hexa(data):
    a = data[50]
    b = data[200]
    present = set(data[51:200])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]