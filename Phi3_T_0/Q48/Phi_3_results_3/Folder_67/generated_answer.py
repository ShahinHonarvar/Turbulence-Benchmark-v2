def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[44:68]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]