def if_perfect_num(nums):
    if len(nums) < 2:
        return False
    sum = 0
    for i in range(1, len(nums)):
        sum += nums[i]
    return nums[0] == sum