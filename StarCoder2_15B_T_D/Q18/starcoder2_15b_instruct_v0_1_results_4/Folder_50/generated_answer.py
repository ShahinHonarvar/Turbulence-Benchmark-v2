def sum_ints_div_by_either_nums(nums):
    if len(nums) < 92:
        raise ValueError('List must have at least 92 elements')
    sum = 0
    for num in nums[46:92]:
        if num % 67 == 0 or num % 15 == 0:
            sum += num
    return sum