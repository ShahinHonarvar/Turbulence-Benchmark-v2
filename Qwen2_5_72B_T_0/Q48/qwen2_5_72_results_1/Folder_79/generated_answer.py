def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[2:7]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((0, 1, 2, 3, 4, 5, 6, 8, 9, 10), '7'), ((0, 1, 2, 3, 4, 5, 6, 10, 11, 12), '1e'), ((0, 1, 3, 4, 5, 6, 7, 9, 10, 11), '8'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), '')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for input: {input_tuple}'
    print('All test cases passed.')