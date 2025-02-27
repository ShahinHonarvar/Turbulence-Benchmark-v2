def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ''), ([1, 2, 3, 5, 7, 9, 11, 13, 15, 17], '2c'), ([0, 1, 2, 4, 6, 8, 10, 12, 14, 16], '3e8'), ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], '1100000')]
    for input_tuple, expected in test_cases:
        result = return_binary_or_hexa(input_tuple)
        assert result == expected, f'Failed for {input_tuple}, expected {expected} but got {result}'
    print('All test cases passed.')