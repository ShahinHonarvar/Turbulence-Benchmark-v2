def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[a + 1:b]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]