def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[14:70]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_data = tuple(range(100))
    assert return_binary_or_hexa(test_data) == '', 'Test case 1 failed'
    test_data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 34, 35, 37, 38, 40, 42, 44, 45, 47, 48, 50, 52, 54, 55, 57, 58, 60, 62, 64, 65, 67, 68, 70, 72, 74, 75, 77, 79, 81, 83, 85, 86, 88, 90, 92, 93, 95, 97, 99)
    assert return_binary_or_hexa(test_data) == '12c', 'Test case 2 failed'
    print('All test cases passed.')