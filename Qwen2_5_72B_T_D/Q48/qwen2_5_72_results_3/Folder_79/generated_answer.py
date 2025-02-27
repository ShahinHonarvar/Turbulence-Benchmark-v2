def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    present_numbers = set(numbers[2:7])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    test_cases = [((0, 5, 6, 7, 8, 9, 10, 15), '63'), ((0, 1, 2, 3, 4, 5, 6, 10), '28'), ((0, 1, 2, 3, 4, 5, 6, 7), '')]
    for nums, expected in test_cases:
        result = return_binary_or_hexa(nums)
        assert result == expected, f'Expected {expected}, got {result} for input {nums}'
    print('All test cases passed!')