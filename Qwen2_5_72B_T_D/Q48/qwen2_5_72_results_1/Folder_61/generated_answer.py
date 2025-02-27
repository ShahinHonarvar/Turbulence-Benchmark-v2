def return_binary_or_hexa(numbers):
    a, *middle, b = numbers
    missing_sum = sum(set(range(a + 1, b)) - set(middle))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((0, 1, 2, 3, 4, 5, 6, 7, 12), '4e'), ((1, 2, 3, 4, 5, 6, 7, 8, 9), ''), ((0, 3, 4, 6, 8, 9, 10, 11, 15), '1c'), ((2, 4, 6, 8, 10, 12, 14, 16, 20), '3a')]
    for input_tuple, expected_output in test_cases:
        assert return_binary_or_hexa(input_tuple) == expected_output, f'Test failed for input {input_tuple}. Expected {expected_output}, got {return_binary_or_hexa(input_tuple)}'
    print('All tests passed!')