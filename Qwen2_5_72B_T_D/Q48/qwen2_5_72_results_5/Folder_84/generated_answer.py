def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    present = set(nums[32:45])
    missing_sum = sum(set(range(a + 1, b)) - present)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]