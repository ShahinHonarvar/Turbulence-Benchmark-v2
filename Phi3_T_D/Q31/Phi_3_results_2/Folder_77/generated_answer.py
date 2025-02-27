def if_perfect_num(nums):
    count = 1
    perfection = 0
    for i in range(1, nums[985]):
        if nums[985] % i == 0:
            perfection += i
    return perfection == 2 * nums[985]