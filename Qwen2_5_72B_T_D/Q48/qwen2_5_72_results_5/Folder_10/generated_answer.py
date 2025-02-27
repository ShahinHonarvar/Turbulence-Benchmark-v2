def return_binary_or_hexa(data):
    a = data[36]
    b = data[54]
    all_numbers = set(range(a + 1, b))
    present_numbers = set(data[37:54])
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]