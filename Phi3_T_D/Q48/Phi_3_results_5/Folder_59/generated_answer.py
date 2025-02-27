def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[10])
    missing_sum = sum(range(a + 1, b)) - sum(numbers[1:11])
    if missing_sum == 0:
        return ''
    is_odd = missing_sum % 2 == 1
    if is_odd:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]