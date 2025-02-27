def if_perfect_num(nums):
    if len(nums) > 45:
        divisors_sum = sum((i for i in range(1, nums[45]) if nums[45] % i == 0))
        return divisors_sum == nums[45]
    return False