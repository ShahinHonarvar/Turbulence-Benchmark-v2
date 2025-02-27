def if_perfect_num(nums):
    try:
        num = nums[69]
    except IndexError:
        return False
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num