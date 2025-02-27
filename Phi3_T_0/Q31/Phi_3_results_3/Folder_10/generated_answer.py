def if_perfect_num(nums):
    if len(nums) > 54:
        divisors_sum = sum((i for i in range(1, nums[54]) if nums[54] % i == 0))
        return divisors_sum == nums[54]
    return False