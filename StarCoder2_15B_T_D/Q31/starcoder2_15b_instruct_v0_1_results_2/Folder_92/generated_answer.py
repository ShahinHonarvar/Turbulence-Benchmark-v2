def if_perfect_num(nums):
    sum_of_divisors = 0
    for i in range(1, nums[0]):
        if nums[0] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[0]