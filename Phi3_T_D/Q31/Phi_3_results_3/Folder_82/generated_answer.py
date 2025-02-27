def if_perfect_num(nums):
    try:
        num = nums[83]
    except IndexError:
        return False
    divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    return sum(divisors) == num