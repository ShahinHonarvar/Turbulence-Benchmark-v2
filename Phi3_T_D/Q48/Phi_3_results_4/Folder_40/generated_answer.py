def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[0] + 1, nums[3] + 1)).difference(nums[1:nums[3]]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')