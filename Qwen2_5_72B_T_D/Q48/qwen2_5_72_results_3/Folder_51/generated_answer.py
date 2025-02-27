def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[7:9]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()

def check_solution():
    test_cases = [([1, 2, 3, 4, 5, 6, 8, 9, 10, 12], 'A'), ([1, 2, 3, 4, 5, 6, 8, 9, 11, 12], '10'), ([1, 2, 3, 4, 5, 6, 8, 10, 11, 12], '')]
    for nums, expected in test_cases:
        result = return_binary_or_hexa(tuple(nums))
        assert result == expected, f'Expected {expected}, but got {result} for input {nums}'
    print('All test cases passed.')