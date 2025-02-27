def if_perfect_num(nums):
    """
    This function takes a list of positive integers and checks if the integer at index 84 is a perfect number.
    If it is a perfect number, the function returns True, otherwise it returns False.
    """
    sum_of_divisors = 0
    num = nums[84]
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num