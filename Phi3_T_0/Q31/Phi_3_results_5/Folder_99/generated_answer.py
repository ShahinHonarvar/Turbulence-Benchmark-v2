def if_perfect_num(nums):
    if len(nums) > 733:
        sum_divisors = sum((i for i in range(1, nums[733]) if nums[733] % i == 0))
        return sum_divisors == nums[733]
    return False