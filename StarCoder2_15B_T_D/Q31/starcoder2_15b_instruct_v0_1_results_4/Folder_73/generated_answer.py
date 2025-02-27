def if_perfect_num(nums):
    """
    This function takes a list of positive integers as input and returns True if the integer at index 41 is a perfect number, otherwise it returns False.
    """
    sum_of_factors = 0
    num = nums[41]
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    return sum_of_factors == num