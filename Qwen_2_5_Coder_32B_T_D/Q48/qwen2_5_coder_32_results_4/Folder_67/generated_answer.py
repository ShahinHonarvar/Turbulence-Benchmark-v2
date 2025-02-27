def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    full_range_sum = sum(range(a + 1, b))
    given_range_sum = sum(set(numbers[45:67]))
    diff_sum = full_range_sum - given_range_sum
    if diff_sum == 0:
        return ''
    if diff_sum % 2 == 1:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]