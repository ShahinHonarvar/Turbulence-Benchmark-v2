def if_perfect_num(nums):
    """
    Returns True if the integer at index 63 is a perfect number, otherwise returns False.
    """

    def is_perfect_num(n):
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == n
    return is_perfect_num(nums[63])