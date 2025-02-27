def if_perfect_num(nums):
    """
    This function checks if the integer at index 19 is a perfect number.
    """
    num = nums[19]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num