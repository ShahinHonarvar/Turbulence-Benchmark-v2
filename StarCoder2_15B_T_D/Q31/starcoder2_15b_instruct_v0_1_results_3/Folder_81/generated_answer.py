def if_perfect_num(nums):
    if len(nums) > 20:
        num = nums[20]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False