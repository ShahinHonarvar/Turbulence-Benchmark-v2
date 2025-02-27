def is_perfect_num(nums):
    if len(nums) <= 23:
        return False
    target_num = nums[23]
    divisors_sum = sum([i for i in range(1, target_num) if target_num % i == 0])
    return divisors_sum == target_num