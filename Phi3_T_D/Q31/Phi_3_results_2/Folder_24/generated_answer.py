def if_perfect_num(nums):
    try:
        num = nums[74]
        divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
        return divisors_sum == num
    except IndexError:
        return False