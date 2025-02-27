def if_perfect_num(nums):
    if len(nums) > 849:
        div_sum = sum((i for i in range(1, nums[849]) if nums[849] % i == 0))
        return div_sum == nums[849]
    return False