def if_perfect_num(nums):
    index = 53
    if len(nums) > index:
        num = nums[index]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False