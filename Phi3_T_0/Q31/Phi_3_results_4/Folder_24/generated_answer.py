def if_perfect_num(nums):
    if len(nums) > 74:
        divisors_sum = sum((i for i in range(1, nums[74]) if nums[74] % i == 0))
        return divisors_sum == nums[74]
    return False