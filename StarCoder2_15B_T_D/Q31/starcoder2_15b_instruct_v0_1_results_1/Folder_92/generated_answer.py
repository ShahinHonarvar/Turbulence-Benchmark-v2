def if_perfect_num(nums):
    if nums[0] <= 0:
        return False
    sum_divisors = 0
    for i in range(1, nums[0] // 2 + 1):
        if nums[0] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[0]