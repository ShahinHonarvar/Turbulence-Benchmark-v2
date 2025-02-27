def if_perfect_num(nums):
    if len(nums) < 75:
        return False
    number = nums[74]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number