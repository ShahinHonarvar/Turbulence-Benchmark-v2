def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[2:5]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]