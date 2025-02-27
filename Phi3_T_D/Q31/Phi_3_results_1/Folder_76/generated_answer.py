def if_perfect_num(nums):
    if len(nums) > 537:
        sum_divisors = sum((i for i in range(1, nums[537] // 2 + 1) if nums[537] % i == 0))
        return sum_divisors == nums[537]
    return False