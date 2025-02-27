def if_perfect_num(nums):
    if len(nums) > 72:
        divisors = [i for i in range(1, nums[72] // 2 + 1) if nums[72] % i == 0]
        return sum(divisors) == nums[72]
    return False