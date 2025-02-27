def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()

def check_solution():
    test_cases = [([1, 2, 3, 4, 5, 7, 9, 10, 12], '5'), ([1, 2, 3, 4, 5, 6, 8, 11, 13], 'A'), ([1, 2, 3, 4, 5, 6, 8, 9, 10], '')]
    for case, expected in test_cases:
        assert return_binary_or_hexa(case) == expected, f'Failed for {case}'
    print('All test cases passed.')