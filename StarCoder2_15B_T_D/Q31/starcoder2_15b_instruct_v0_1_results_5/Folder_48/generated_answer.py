def if_perfect_num(nums):
    sum = 0
    for i in range(1, nums[247] // 2 + 1):
        if nums[247] % i == 0:
            sum += i
    return sum == nums[247]