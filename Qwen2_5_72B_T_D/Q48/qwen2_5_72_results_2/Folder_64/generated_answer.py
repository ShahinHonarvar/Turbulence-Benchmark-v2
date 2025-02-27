def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[5]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:5]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((1, 2, 3, 4, 5, 7), '11'), ((0, 2, 4, 6, 8, 10), '18'), ((10, 12, 14, 16, 18, 20), '32'), ((5, 6, 7, 8, 9, 10), '')]
    for input_val, expected_output in test_cases:
        assert return_binary_or_hexa(input_val) == expected_output, f'Failed for {input_val}'
    print('All test cases passed!')