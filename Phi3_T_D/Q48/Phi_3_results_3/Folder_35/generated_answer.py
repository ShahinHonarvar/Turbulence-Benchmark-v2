def return_binary_or_hexa(nums):
    try:
        a = nums[77]
        b = nums[84]
    except IndexError:
        return ''
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in nums[77:84 + 1]))
    if missing_numbers_sum % 2 == 0:
        return format(missing_numbers_sum, 'x')
    else:
        return bin(missing_numbers_sum)[2:]