def return_binary_or_hexa(data):
    a, b = (data[72], data[93])
    absent_sum = sum((i for i in range(a + 1, b) if i not in data[a + 1:b]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return '{:b}'.format(absent_sum)