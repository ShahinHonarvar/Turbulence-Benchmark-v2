def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    existing_numbers = set(numbers[1:10])
    missing_sum = sum(set(range(a + 1, b)) - existing_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_cases = [((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15), '3c'), ((0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12), '1b'), ((5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20), '')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Failed for {input_tuple}'
    print('All test cases passed.')