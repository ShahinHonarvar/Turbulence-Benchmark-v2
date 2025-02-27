def if_perfect_num(num_list):
    """
    This function takes a list of positive integers as an argument and checks if the integer at index 4 is a perfect number.
    """
    if num_list[4] == sum((i for i in range(1, num_list[4]) if num_list[4] % i == 0)):
        return True
    else:
        return False