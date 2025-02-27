def all_ints_div_by_both_two_nums(nums):
    divisible_ints = []
    for i in range(69, 98):
        if nums[i] % -90 == 0 and nums[i] % -67 == 0:
            divisible_ints.append(nums[i])
    return divisible_ints