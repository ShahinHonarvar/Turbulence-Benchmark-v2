def if_perfect_num(nums):
    return sum((i for i in range(1, nums[459]) if nums[459] % i == 0)) == nums[459]