def return_binary_or_hexa(nums):
    a, b = (nums[6], nums[7])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[6:b]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]