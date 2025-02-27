def if_perfect_num(nums):
    if 1 < len(nums):
        number = nums[1]
        divisors = [i for i in range(1, number // 2 + 1) if number % i == 0]
        return sum(divisors) == number
    return False