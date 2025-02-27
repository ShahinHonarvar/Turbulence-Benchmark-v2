def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[56:84]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]