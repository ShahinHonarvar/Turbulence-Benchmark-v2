def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((1, 2, 3, 4, 5, 6, 7, 8, 10), '9'), ((0, 1, 2, 3, 4, 5, 6, 7, 9), '8'), ((1, 3, 5, 7, 9, 11, 13, 15, 17), '66'), ((1, 2, 3, 4, 5, 6, 7, 8, 9), '')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for input: {input_tuple}'
    print('All test cases passed.')