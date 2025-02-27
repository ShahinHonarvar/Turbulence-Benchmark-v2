def if_perfect_num(nums):
    """
    Returns true if the integer at index 126 is a perfect number, otherwise, returns false.
    """
    num = nums[126]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num