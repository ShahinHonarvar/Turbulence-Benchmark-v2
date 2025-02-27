def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    inclusive_range = range(a + 1, b)
    missing_sum = sum((n for n in inclusive_range if n not in nums[933:996 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    return bin(missing_sum)[2:]