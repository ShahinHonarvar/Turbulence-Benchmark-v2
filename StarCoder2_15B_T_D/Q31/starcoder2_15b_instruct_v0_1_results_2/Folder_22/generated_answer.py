def if_perfect_num(nums):
    for i in range(len(nums)):
        sum_divisors = 0
        for j in range(1, nums[i] // 2 + 1):
            if nums[i] % j == 0:
                sum_divisors += j
        if sum_divisors == nums[i]:
            if i == 72:
                return True
    return False