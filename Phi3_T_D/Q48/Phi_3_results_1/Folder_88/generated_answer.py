def return_binary_or_hexa(data):
    a, *_, b = data
    missing_sum = sum((i for i in range(a + 1, b) if i not in data[3:9]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')