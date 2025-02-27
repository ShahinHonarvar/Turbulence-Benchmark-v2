def if_perfect_num(lst):
    """
    Returns True if the integer at index 132 is a perfect number, otherwise returns False.
    """
    n = lst[132]
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n