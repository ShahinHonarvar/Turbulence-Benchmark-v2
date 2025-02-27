def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[90:200]:
        if num % -31 != 0:
            result.append(num)
    return result