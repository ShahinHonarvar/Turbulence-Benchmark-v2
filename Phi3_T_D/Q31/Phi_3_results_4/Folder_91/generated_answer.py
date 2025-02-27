def if_perfect_num(nums):
    if len(nums) < 7:
        return False
    target_num = nums[6]
    sum_of_divisors = sum((i for i in range(1, target_num) if target_num % i == 0))
    return sum_of_divisors == target_num