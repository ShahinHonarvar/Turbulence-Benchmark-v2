def return_binary_or_hexa(nums):
    a, b = (nums[46], nums[91])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[46:91]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()