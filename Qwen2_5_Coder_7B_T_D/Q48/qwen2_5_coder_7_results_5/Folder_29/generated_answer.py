def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[70:99]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()