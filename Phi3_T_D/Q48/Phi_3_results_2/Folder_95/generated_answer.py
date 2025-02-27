def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    not_present_sum = sum(set(range(a + 1, b)).difference(numbers[32:99 + 1]))
    if not_present_sum == 0:
        return ''
    elif not_present_sum % 2 == 1:
        return bin(not_present_sum)[2:]
    else:
        return hex(not_present_sum)[2:]