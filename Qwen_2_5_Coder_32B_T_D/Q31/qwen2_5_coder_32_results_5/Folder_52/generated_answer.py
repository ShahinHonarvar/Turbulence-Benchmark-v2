def if_perfect_num(nums):
    if len(nums) < 479:
        return False
    num = nums[478]
    sum_divisors = sum((d for d in range(1, num) if num % d == 0))
    return sum_divisors == num