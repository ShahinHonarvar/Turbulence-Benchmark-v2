def if_perfect_num(nums):
    if len(nums) <= 276:
        return False
    sum_divisors = 0
    for i in range(1, nums[276]):
        if nums[276] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[276]