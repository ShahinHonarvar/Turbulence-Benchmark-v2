def if_perfect_num(nums):
    if len(nums) < 101:
        return False
    sum_of_divisors = 0
    for i in range(1, nums[100]):
        if nums[100] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[100]