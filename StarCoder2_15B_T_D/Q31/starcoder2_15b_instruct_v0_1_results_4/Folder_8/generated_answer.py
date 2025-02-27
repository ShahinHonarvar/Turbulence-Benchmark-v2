def if_perfect_num(nums):
    sum_divisors = 0
    for i in range(1, nums[49]):
        if nums[49] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[49]