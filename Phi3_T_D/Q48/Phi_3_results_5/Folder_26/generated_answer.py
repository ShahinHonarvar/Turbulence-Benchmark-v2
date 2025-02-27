def return_binary_or_hexa(numbers):
    a, b = (numbers[68], numbers[99])
    missing_sum = sum(set(range(a + 1, b)).difference(set(numbers[68:99])))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return bin(missing_sum)[2:]