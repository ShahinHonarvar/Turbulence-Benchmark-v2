def if_perfect_num(nums):
    if len(nums) > 321:
        sum_divisors = sum((i for i in range(1, nums[321]) if nums[321] % i == 0))
        return sum_divisors == nums[321]
    return False