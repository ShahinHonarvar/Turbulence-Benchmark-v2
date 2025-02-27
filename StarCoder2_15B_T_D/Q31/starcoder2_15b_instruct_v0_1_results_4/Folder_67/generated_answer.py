def if_perfect_num(nums):
    """
    Takes a list of positive integers and returns True if the integer at index 43 is a perfect number, otherwise, returns False.
    """
    num = nums[43]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num