def if_perfect_num(nums):
    i = 17
    sum_divisors = 0
    for j in range(1, nums[i]):
        if nums[i] % j == 0:
            sum_divisors += j
    return sum_divisors == nums[i]