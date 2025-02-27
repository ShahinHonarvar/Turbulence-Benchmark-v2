def return_binary_or_hexa(data):
    a = data[200]
    b = data[202]
    existing_numbers = set(data[201:202])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]