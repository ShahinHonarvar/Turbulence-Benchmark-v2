def if_perfect_num(nums):
    sum_of_nums = 0
    for i in range(len(nums)):
        sum_of_nums += nums[i]
    if sum_of_nums == nums[4]:
        return True
    else:
        return False