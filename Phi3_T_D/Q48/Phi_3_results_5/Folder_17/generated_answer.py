def return_binary_or_hexa(nums):
    a = nums[73] + 1
    b = nums[84] - 1
    missing_sum = sum((i for i in range(a, b + 1) if i not in nums[73:85]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]