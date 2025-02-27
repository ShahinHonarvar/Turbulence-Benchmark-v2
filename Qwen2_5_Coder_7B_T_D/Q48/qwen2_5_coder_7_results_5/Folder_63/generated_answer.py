def return_binary_or_hexa(nums):
    a, b = (nums[81], nums[86])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[81:87]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]