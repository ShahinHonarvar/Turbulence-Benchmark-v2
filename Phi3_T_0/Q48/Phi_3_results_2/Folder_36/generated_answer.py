def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[110:348 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]