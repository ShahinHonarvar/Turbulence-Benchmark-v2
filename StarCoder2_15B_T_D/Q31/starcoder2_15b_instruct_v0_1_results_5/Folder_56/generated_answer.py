def if_perfect_num(nums):
    """
    This function takes a list of positive integers as input and returns True if the integer at index 60 is a perfect number, otherwise it returns False.
    """

    def is_perfect_num(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    return is_perfect_num(nums[60])