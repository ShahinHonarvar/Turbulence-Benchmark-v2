def if_perfect_num(nums):
    if len(nums) < 3:
        return False
    num = nums[2]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num