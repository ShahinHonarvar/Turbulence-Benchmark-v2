def return_binary_or_hexa(nums):
    a, b = (nums[27], nums[96])
    absent_sum = sum(set(range(a + 1, b)) - set(nums[27:96])) - (min(nums[27:96]) - a - 1 - (b - min(nums[27:96]) - 1))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]