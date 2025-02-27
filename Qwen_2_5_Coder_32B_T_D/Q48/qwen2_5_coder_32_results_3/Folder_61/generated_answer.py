def return_binary_or_hexa(tup):
    a, *_, b = tup
    total_sum = 0
    present_numbers = set(tup)
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]