def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[5]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[3:5]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_cases = [((1, 2, 3, 5, 7, 9, 10), '1110', 'the sum is 14, even, so hex is returned'), ((1, 2, 3, 5, 7, 8, 10), '', 'all numbers are present, so nothing is returned'), ((1, 2, 3, 6, 8, 9, 10), '10000', 'the sum is 16, but since 7 is missing, the sum is 7, so binary is returned')]
    for test, expected, _ in test_cases:
        result = return_binary_or_hexa(test)
        assert result == expected, f'Test failed for {test}. Expected {expected}, got {result}.'
    print('All tests passed.')