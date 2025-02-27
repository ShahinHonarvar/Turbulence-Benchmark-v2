def if_perfect_num(nums):
    sum_of_divisors = 0
    for i in range(1, nums[42]):
        if nums[42] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == nums[42]