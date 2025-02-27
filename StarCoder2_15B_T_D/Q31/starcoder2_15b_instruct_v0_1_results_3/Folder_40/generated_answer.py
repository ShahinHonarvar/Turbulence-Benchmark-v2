def if_perfect_num(nums):
    if len(nums) < 8:
        return False
    sum_of_divisors = 0
    for i in range(1, nums[7]):
        if nums[7] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[7]