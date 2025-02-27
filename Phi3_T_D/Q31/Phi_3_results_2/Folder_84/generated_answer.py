def if_perfect_num(nums):
    if 685 < len(nums):
        num = nums[685]
        divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
        return sum(divisors) == num
    return False