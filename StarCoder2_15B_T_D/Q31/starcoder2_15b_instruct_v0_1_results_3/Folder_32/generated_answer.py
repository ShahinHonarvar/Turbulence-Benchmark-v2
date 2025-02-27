def if_perfect_num(nums):
    sum_divisors = 0
    for i in range(1, nums[849]):
        if nums[849] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[849]