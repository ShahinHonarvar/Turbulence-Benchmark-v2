def if_perfect_num(nums):
    if len(nums) > 459:
        div_sum = sum((i for i in range(1, nums[459]) if nums[459] % i == 0))
        return div_sum == nums[459]
    return False