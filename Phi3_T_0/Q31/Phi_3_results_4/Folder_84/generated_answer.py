def if_perfect_num(nums):
    if len(nums) > 685:
        div_sum = sum((i for i in range(1, nums[685]) if nums[685] % i == 0))
        return div_sum == nums[685]
    return False