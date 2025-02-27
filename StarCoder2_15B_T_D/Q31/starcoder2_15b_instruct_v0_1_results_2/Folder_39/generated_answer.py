def if_perfect_num(nums):
    divisors = [i for i in range(1, nums[59]) if nums[59] % i == 0]
    return sum(divisors) == nums[59]