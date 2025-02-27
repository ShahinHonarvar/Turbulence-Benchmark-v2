def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    subset = set(numbers[19:60])
    missing_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_numbers = tuple(range(100))
    result = return_binary_or_hexa(test_numbers)
    assert result == '', 'Test case 1 failed'
    test_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
    result = return_binary_or_hexa(test_numbers)
    assert result == '100110', 'Test case 2 failed'
    print('All tests passed!')