def if_perfect_num(nums):
    """
    Returns true if the integer at index 13 is a perfect number, otherwise, it returns false.
    """
    num = nums[13]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num