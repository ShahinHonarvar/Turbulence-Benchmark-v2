def if_perfect_num(nums):
    if len(nums) <= 47:
        return False
    target = nums[47]
    if target < 1:
        return False
    divisors_sum = sum([i for i in range(1, target) if target % i == 0])
    return divisors_sum == target