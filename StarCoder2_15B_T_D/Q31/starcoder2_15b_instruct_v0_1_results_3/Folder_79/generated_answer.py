def if_perfect_num(nums):
    if len(nums) > 63:
        sum_of_divisors = 0
        for i in range(1, nums[63] // 2 + 1):
            if nums[63] % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == nums[63]:
            return True
    return False