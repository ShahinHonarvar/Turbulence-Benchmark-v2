def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[73:93]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    nums = tuple(range(100))
    assert return_binary_or_hexa(nums) == '', 'Test case 1 failed'
    nums = tuple(list(range(100))[:72] + [100] + list(range(73, 100)))
    assert return_binary_or_hexa(nums) == '63', 'Test case 2 failed'
    nums = tuple(list(range(100))[:72] + [100, 101, 102] + list(range(73, 100))[3:])
    assert return_binary_or_hexa(nums) == '1ec', 'Test case 3 failed'
    print('All test cases passed!')