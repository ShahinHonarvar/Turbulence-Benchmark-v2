def if_perfect_num(nums):
    divisor_sum = 0
    for i in range(1, nums[990] // 2 + 1):
        if nums[990] % i == 0:
            divisor_sum += i
    return divisor_sum == nums[990]