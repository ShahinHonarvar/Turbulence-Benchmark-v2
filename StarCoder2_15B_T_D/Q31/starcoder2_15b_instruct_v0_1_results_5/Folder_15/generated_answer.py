def if_perfect_num(nums):
    sum = 0
    for i in range(1, nums[10] + 1):
        if nums[10] % i == 0:
            sum += i
    if sum == nums[10]:
        return True
    return False