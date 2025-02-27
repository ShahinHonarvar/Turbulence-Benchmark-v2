def if_perfect_num(nums):
    if len(nums) > 126:
        divisors_sum = sum((i for i in range(1, nums[126] // 2 + 1) if nums[126] % i == 0))
        return divisors_sum == nums[126]
    return False