def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    existing_values = set(nums[20:32])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_values))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]