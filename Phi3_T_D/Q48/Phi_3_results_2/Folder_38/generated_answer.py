def return_binary_or_hexa(nums):
    start, end = (nums[36], nums[85])
    missing_sum = sum((i for i in range(start + 1, end) if i not in nums))
    if missing_sum % 2 == 0:
        return '{:X}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum).lstrip('0')