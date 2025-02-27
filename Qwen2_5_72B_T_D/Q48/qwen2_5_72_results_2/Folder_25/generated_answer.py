def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[38:43]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_case = tuple(range(100))
    assert return_binary_or_hexa(test_case) == '', 'Test case 1 failed'
    test_case = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 40, 42, 44, 45, 46, 47, 48, 49, 50)
    assert return_binary_or_hexa(test_case) == '110', 'Test case 2 failed'
    test_case = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 45, 46, 47, 48, 49, 50)
    assert return_binary_or_hexa(test_case) == '3e', 'Test case 3 failed'
    print('All test cases passed')