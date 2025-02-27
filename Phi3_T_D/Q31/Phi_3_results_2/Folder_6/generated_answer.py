def if_perfect_num(nums):
    if len(nums) > 790 and all((isinstance(x, int) and x > 0 for x in nums[:791])):
        num = nums[790]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False