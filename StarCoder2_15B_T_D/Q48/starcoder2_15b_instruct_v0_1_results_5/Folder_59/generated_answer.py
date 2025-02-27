def return_binary_or_hexa(nums):
    sum_of_missing_nums = 0
    for i in range(nums[0] + 1, nums[10] - 1):
        if i not in nums:
            sum_of_missing_nums += i
    if sum_of_missing_nums % 2 == 1:
        return format(sum_of_missing_nums, 'b')
    elif sum_of_missing_nums % 2 == 0:
        return format(sum_of_missing_nums, 'x')
    else:
        return ''