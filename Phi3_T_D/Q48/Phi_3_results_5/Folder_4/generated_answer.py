def return_binary_or_hexa(nums):
    a = nums[49]
    b = nums[74]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[49:74 + 1]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]