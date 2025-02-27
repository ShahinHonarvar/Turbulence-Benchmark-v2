def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), '1c'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), '1c'), ((0, 1, 2, 4, 6, 8, 10, 12, 14, 16), '1e'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 10), '')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for input: {input_tuple}'
    print('All test cases passed.')