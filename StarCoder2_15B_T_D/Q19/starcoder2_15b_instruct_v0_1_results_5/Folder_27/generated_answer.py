def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[14:21]:
        if num % -93 != 0:
            result.append(num)
    return result