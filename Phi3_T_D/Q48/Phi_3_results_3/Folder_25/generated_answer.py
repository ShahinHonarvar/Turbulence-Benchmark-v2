def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[37:43]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return f'{bin(missing_sum)[2:].upper()}'