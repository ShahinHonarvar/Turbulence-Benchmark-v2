def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    available_nums = set(range(a + 1, b))
    missing_nums = available_nums - set(nums[28:96])
    total_sum = sum(missing_nums)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_function():
    test_data = tuple(list(range(100)))
    assert return_binary_or_hexa(test_data) == '1588', 'Test case 1 failed'
    test_data = tuple([0] + list(range(30, 130)))
    assert return_binary_or_hexa(test_data) == '11110110001000', 'Test case 2 failed'
    test_data = tuple([x for x in range(150) if x != 120])
    assert return_binary_or_hexa(test_data) == '111011100000', 'Test case 3 failed'
    print('All test cases passed.')