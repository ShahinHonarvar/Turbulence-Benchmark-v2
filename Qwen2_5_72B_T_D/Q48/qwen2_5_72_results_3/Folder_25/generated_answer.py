def return_binary_or_hexa(nums):
    if len(nums) < 44:
        return ''
    a = nums[37]
    b = nums[43]
    existing_values = set(nums[38:43])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_values))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]