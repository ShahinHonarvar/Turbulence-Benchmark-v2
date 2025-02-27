def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[7]
    missing_sum = sum([i for i in range(a + 1, b) if i not in nums[2:8]])
    if missing_sum % 2 == 0:
        return f'{missing_sum:#x}'
    else:
        return f'{missing_sum:b}'[2:]