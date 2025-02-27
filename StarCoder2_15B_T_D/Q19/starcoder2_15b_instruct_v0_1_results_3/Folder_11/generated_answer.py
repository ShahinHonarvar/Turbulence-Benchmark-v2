def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[36:85]:
        if num % -27 != 0:
            result.append(num)
    return result