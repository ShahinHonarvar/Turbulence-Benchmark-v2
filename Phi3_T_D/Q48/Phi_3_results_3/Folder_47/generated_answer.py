def return_binary_or_hexa(nums):
    a, b = (nums[29], nums[53])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[29:54]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()