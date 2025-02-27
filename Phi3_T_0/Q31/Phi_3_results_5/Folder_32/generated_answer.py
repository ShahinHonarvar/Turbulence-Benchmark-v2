def if_perfect_num(nums):
    if len(nums) > 849:
        sum_of_divisors = sum((i for i in range(1, nums[849]) if nums[849] % i == 0))
        return sum_of_divisors == nums[849]
    return False