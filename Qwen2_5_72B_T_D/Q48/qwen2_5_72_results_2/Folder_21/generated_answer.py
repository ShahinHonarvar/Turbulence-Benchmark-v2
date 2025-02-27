def return_binary_or_hexa(data):
    a = data[15]
    b = data[57]
    present_numbers = set(data[16:57])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]