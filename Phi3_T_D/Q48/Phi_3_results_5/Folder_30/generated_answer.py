def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    missing_sum = sum([num for num in range(a + 1, b) if num not in nums[22:24]])
    if missing_sum % 2:
        return format(missing_sum, 'b').lstrip('0b')
    else:
        return format(missing_sum, 'X').lstrip('0')