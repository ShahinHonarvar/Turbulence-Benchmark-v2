def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[27:97]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]