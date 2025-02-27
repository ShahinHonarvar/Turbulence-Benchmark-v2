def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[6]
    b = nums_tuple[7]
    missing_sum = sum((num for num in range(a + 1, b) if num not in nums_tuple[6:b]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')