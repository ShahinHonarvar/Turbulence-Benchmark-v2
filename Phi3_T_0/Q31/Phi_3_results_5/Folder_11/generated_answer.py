def if_perfect_num(nums):
    if len(nums) > 77:
        divisors_sum = sum((i for i in range(1, nums[77]) if nums[77] % i == 0))
        return divisors_sum == nums[77]
    return False