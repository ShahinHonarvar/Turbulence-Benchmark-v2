def if_perfect_num(nums):
    num = nums[100]
    divisors = [d for d in range(1, num) if num % d == 0]
    return sum(divisors) == num