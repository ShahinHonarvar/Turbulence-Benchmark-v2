def return_binary_or_hexa(numbers):
    if len(numbers) < 6:
        return ''
    a = numbers[2]
    b = numbers[5]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            missing_sum += num
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]

def check_function():
    test_cases = [((1, 2, 3, 7, 9, 11, 12, 14), '14'), ((1, 2, 3, 4, 5, 6, 10, 12), '1011'), ((1, 2, 3, 4, 6, 7, 10, 12), '')]
    for inputs, expected in test_cases:
        result = return_binary_or_hexa(inputs)
        assert result == expected, f'For inputs {inputs}, expected {expected} but got {result}'
    print('All test cases passed.')