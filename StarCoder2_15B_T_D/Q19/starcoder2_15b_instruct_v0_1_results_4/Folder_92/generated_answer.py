def all_ints_not_div_by_num(nums):
    all_ints_not_div_by_num = []
    for num in nums:
        if num % -1 != 0:
            all_ints_not_div_by_num.append(num)
    return all_ints_not_div_by_num