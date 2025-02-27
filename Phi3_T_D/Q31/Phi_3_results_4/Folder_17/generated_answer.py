def if_perfect_num(nums):
    if len(nums) > 632:
        sum_divisors = sum((div for div in range(1, nums[632] // 2 + 1) if nums[632] % div == 0))
        return sum_divisors == nums[632]
    return False