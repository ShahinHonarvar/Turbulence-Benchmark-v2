def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    missing_nums = set(range(a + 1, b)) - set(nums[57:86])
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 1:
        return format(sum_of_missing_nums, 'b')
    else:
        return format(sum_of_missing_nums, 'x')