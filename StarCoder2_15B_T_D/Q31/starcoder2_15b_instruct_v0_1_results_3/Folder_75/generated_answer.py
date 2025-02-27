def if_perfect_num(nums):
    sum_divisors = 0
    for i in range(1, nums[80] // 2 + 1):
        if nums[80] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[80]