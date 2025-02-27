def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[35] + 1, nums[64])) - set(nums[35:65]))
    if missing_sum < 0:
        return ''
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x')