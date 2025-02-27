def return_binary_or_hexa(nums):
    if len(nums) < 98:
        return ''
    a = nums[69]
    b = nums[97]
    present = set(nums[69:98])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    example1 = tuple(range(100))
    example2 = tuple(range(100))
    example3 = tuple(range(100)[::2])
    assert return_binary_or_hexa(example1) == '', 'Test case 1 failed'
    assert return_binary_or_hexa(example2) == '0', 'Test case 2 failed'
    assert return_binary_or_hexa(example3) == '1ef', 'Test case 3 failed'
    print('All test cases passed')