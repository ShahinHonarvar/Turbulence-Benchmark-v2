def return_binary_or_hexa(nums):
    missing_sum = sum({i for i in range(nums[73] + 1, nums[84])} - set(nums[73:85]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]