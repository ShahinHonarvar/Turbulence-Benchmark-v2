def return_binary_or_hexa(nums):
    if len(nums) < 82:
        return ''
    target_range = set(range(nums[38] + 1, nums[81]))
    missing_numbers = target_range.difference(set(nums[38:81]))
    total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 else hex(total)[2:]