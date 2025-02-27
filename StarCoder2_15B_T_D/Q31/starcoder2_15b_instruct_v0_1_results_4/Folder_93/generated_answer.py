def if_perfect_num(lst):
    """
    Returns True if the integer at index 45 is a perfect number, otherwise returns False.
    """
    num = lst[45]
    return sum((divisor for divisor in range(1, num) if num % divisor == 0)) == num