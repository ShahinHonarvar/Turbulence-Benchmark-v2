def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[2:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((0, 1, 2, 3, 4, 5, 6, 7, 10), '18'), ((0, 1, 2, 3, 4, 5, 6, 7, 9), '20'), ((0, 1, 3, 4, 5, 6, 7, 8, 10), '2'), ((0, 1, 2, 3, 4, 5, 6, 7, 8), '')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for {input_tuple}'
    print('All test cases passed.')