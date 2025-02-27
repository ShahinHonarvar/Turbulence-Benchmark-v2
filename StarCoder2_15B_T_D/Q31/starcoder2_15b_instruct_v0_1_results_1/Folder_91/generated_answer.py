def if_perfect_num(nums):
    if len(nums) <= 6:
        return False
    sum_of_divisors = 0
    for i in range(1, nums[6] // 2 + 1):
        if nums[6] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[6]