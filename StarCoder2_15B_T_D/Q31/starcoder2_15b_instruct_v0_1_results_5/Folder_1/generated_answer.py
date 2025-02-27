def if_perfect_num(nums):
    perfect_num = False
    for i in range(len(nums)):
        divisors = [j for j in range(1, nums[i] // 2 + 1) if nums[i] % j == 0]
        if sum(divisors) == nums[i]:
            perfect_num = True
            break
    return perfect_num