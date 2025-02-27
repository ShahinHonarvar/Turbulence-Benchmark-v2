def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[32] + 1, nums[44])) - set(nums[32:45]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]