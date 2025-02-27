def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[21:36]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_case_1 = tuple(range(0, 50))
    test_case_2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
    assert return_binary_or_hexa(test_case_1) == ''
    assert return_binary_or_hexa(test_case_2) == '1c5'
    print('All test cases passed.')