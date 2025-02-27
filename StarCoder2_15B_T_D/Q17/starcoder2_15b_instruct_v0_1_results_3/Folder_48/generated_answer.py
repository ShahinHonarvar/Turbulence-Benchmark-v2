def all_ints_div_by_both_two_nums(nums):
    output = []
    for num in nums[306:958]:
        if num % 982 == 0 and num % 319 == 0:
            output.append(num)
    return output