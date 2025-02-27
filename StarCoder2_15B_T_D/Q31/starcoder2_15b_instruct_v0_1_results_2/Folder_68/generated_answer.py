def if_perfect_num(nums):
    if len(nums) > 3:
        num = nums[3]
        sum_divisors = sum((d for d in range(1, num) if num % d == 0))
        return sum_divisors == num
    return False