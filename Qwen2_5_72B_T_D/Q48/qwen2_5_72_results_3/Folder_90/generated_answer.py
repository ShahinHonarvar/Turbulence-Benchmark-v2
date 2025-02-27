def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[61:90]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_tuple = tuple(range(100))
    result = return_binary_or_hexa(test_tuple)
    assert result == '', 'When all numbers are present, the result should be an empty string.'
    test_tuple_with_gaps = test_tuple[:61] + (65, 66, 67, 68, 69, 70, 72, 73, 74, 76, 78, 80, 82, 84, 86, 88, 97) + test_tuple[91:]
    result = return_binary_or_hexa(test_tuple_with_gaps)
    assert result == '1011000000110000', 'The sum of missing numbers should be correctly converted to binary.'