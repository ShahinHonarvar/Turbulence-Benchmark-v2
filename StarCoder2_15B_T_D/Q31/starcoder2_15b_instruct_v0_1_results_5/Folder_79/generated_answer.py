def if_perfect_num(lst):
    """
    Returns True if the integer at index 63 is a perfect number, otherwise returns False.

    Parameters:
    lst (list): A list of positive integers.

    Returns:
    bool: True if the integer at index 63 is a perfect number, otherwise False.
    """

    def factors_sum(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum
    return factors_sum(lst[63]) == lst[63]