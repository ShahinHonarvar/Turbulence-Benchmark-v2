def return_binary_or_hexa(nums):
    a, b = (nums[6], nums[9])
    target_range = set(range(a + 1, b))
    present_range = set(nums[6:9])
    missing_numbers = target_range - present_range
    if missing_numbers:
        total_sum = sum(missing_numbers)
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:].upper()
    else:
        return ''