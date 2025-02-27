def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[1:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test1 = (1, 2, 3, 4, 5, 6, 7, 8, 10)
    test2 = (0, 2, 3, 4, 5, 6, 7, 8, 11)
    test3 = (1, 2, 3, 4, 5, 6, 7, 9, 11)
    assert return_binary_or_hexa(test1) == '9', 'Test case 1 failed'
    assert return_binary_or_hexa(test2) == '1e', 'Test case 2 failed'
    assert return_binary_or_hexa(test3) == '', 'Test case 3 failed'
    print('All test cases passed!')