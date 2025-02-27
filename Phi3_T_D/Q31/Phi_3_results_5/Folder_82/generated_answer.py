def is_perfect_num(nums):
    if 83 >= len(nums):
        return False
    number = nums[83]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number