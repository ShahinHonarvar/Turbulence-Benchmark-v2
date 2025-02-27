def if_perfect_num(nums):
    try:
        target = nums[47]
    except IndexError:
        return False
    divisors = [i for i in range(1, target) if target % i == 0]
    return sum(divisors) == target