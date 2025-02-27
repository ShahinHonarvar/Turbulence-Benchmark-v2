def if_perfect_num(nums):
    if len(nums) > 6:
        i = 6
        divisors_sum = sum((number for number in range(1, nums[i] // 2 + 1) if nums[i] % number == 0))
        return divisors_sum == nums[i]
    return False