def return_binary_or_hexa(nums):
    a, b = (nums[18], nums[60])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[18:60]))
    return f'{missing_sum:b}' if missing_sum % 2 else f'{missing_sum:#x}'