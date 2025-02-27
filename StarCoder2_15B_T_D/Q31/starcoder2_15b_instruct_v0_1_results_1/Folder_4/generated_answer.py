def if_perfect_num(lst):
    """
    This function takes a list of positive integers as input and returns True if the integer at index 15 is a perfect number, otherwise it returns False.
    """
    num = lst[15]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num