def if_perfect_num(nums):
    num = nums[132]
    divisors = [n for n in range(1, num) if num % n == 0]
    sum_divisors = sum(divisors)
    if sum_divisors == num:
        return True
    else:
        return False