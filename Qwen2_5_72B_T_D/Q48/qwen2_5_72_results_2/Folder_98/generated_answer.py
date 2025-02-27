def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((0, 1, 2, 3, 4, 5, 8, 10), '1011'), ((1, 2, 3, 4, 5, 6, 7, 9), '8'), ((1, 2, 3, 4, 5, 6, 7, 8), '')]
    for input_tuple, expected in test_cases:
        result = return_binary_or_hexa(input_tuple)
        assert result == expected, f'Failed for {input_tuple}. Expected {expected}, got {result}'
    print('All test cases passed.')