def if_perfect_num(nums):
    """
    Checks if the integer at index 68 is a perfect number.
    """
    num = nums[68]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num