def return_binary_or_hexa(nums):
    a = nums[39]
    b = nums[43]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[40:43]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]