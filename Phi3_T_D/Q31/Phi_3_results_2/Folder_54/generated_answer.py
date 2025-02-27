def if_perfect_num(nums):
    if 51 < len(nums):
        num = nums[51]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False