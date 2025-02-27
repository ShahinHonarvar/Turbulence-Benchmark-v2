def return_binary_or_hexa(nums):
    a = nums[27]
    b = nums[96]
    missing_sum = sum(range(a + 1, b)) - sum(set(nums[28:96]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()