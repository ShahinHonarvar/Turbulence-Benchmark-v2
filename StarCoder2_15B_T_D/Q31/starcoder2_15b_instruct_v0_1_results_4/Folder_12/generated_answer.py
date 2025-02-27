def if_perfect_num(nums):
    if len(nums) < 28:
        return False
    num = nums[27]
    divisors = [d for d in range(1, num) if num % d == 0]
    return sum(divisors) == num