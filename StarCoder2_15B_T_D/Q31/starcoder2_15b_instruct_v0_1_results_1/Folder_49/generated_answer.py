def if_perfect_num(lst):
    """
    Function to check if the integer at index 68 is a perfect number.
    """

    def is_perfect(n):
        """
        Function to check if a given number is perfect.
        """
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == n
    return is_perfect(lst[68])