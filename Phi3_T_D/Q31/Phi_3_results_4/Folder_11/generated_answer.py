def if_perfect_num(nums):
    if 77 < len(nums):
        num = nums[77]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False