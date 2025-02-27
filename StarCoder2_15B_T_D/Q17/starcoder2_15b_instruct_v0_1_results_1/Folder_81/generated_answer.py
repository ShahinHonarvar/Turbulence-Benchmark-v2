def all_ints_div_by_both_two_nums(nums):
    output = []
    for i in range(10, 101):
        if nums[i] % 10 == 0 and nums[i] % 100 == 0:
            output.append(nums[i])
    return output