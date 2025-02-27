def if_perfect_num(nums):
    sum_divisors = 0
    for i in range(1, nums[92] - 1):
        if nums[92] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[92]