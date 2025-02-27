def if_perfect_num(nums):
    if len(nums) < 850:
        return False
    num = nums[849]
    return num == sum((i for i in range(1, num) if num % i == 0))