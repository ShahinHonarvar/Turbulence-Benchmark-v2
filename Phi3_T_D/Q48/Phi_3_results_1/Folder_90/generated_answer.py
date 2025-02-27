def return_binary_or_hexa(nums):
    assert len(nums) > 90, 'Tuple should have at least 91 elements.'
    a = nums[60]
    b = nums[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[60:90]))
    if missing_sum % 2 == 0:
        return f'{missing_sum:x}'
    else:
        return bin(missing_sum)[2:]