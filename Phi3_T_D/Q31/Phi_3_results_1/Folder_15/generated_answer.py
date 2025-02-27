def if_perfect_num(nums):
    sum_of_divisors = sum((i for i in range(1, nums[10]) if nums[10] % i == 0))
    return sum_of_divisors == nums[10] + 1