def if_perfect_num(nums):
    if len(nums) < 7:
        return False
    num = nums[6]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num