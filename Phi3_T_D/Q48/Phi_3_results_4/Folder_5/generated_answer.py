def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[8])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:8 + 1]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]