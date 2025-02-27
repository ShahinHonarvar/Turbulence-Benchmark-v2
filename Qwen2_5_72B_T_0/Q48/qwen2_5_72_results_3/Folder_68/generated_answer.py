def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((1, 2, 3, 4, 5, 6, 7, 8, 9, 11), '1a'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 10), '1'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ''), ((10, 11, 12, 13, 14, 15, 16, 17, 18, 20), '1e')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for {input_tuple}'
    print('All test cases passed.')