def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[22] + 1, nums[24])) - set(nums[22:nums[24]]))
    return bin(missing_sum)[2:] if missing_sum % 2 else '{:x}'.format(missing_sum)