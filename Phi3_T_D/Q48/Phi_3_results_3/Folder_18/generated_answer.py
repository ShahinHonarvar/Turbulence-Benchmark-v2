def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[56:91]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    return bin(missing_sum)[2:]