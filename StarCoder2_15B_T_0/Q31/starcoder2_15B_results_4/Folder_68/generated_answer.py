def if_perfect_num(nums):
    """
    This function takes a list of positive integers as input and returns True if the integer at index 3 is a perfect number, otherwise it returns False.
    """
    num = nums[3]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num