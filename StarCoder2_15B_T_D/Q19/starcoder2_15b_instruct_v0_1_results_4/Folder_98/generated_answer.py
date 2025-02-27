def all_ints_not_div_by_num(nums):
    result = []
    for num in nums:
        if num % 13 != 0:
            result.append(num)
    return result