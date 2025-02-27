def all_ints_not_div_by_num(nums):
    nums_not_div_by_num = []
    for num in nums:
        if num % -68 != 0:
            nums_not_div_by_num.append(num)
    return nums_not_div_by_num