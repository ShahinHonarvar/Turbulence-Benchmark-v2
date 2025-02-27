def if_perfect_num(nums):
    sum_divisors = 0
    for i in range(1, nums[60] // 2 + 1):
        if nums[60] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[60]