def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[8]
    missing_sum = sum(range(a + 1, b), 0) - sum(nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]