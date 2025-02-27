def if_perfect_num(nums):
    """
    This function checks if the integer at index 51 is a perfect number.
    """
    num = nums[51]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num