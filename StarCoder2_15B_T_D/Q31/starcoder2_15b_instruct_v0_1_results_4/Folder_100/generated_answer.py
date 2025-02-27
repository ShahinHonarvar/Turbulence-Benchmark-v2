def if_perfect_num(nums):
    for i in range(100, len(nums)):
        divisor_sum = sum((divisor for divisor in range(1, nums[i] // 2 + 1) if nums[i] % divisor == 0))
        if divisor_sum == nums[i]:
            return True
    return False