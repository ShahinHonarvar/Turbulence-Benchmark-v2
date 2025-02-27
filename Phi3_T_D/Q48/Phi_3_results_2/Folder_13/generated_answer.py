def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[46] + 1, nums[91])) - set(nums[46:91 + 1]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()