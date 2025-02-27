def return_binary_or_hexa(nums):
    missing_numbers = set(range(nums[0] + 1, nums[9])) - set(nums)
    missing_sum = sum(missing_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()