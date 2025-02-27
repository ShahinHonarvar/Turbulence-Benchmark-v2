def if_perfect_num(nums):
    """
    Returns True if the integer at index 21 is a perfect number, otherwise returns False.
    """
    num = nums[21]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num