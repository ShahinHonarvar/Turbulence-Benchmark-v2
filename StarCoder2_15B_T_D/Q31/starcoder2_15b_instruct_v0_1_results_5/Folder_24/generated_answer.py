def if_perfect_num(nums):
    sum_of_divisors = 0
    for i in range(1, nums[74]):
        if nums[74] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[74]