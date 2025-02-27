from index 639 to index 975, both inclusive. If no odd integers exist in the specified

def sum_odd_ints_inclusive(integer_list):
    """
    This function takes a list of integers as input and returns the sum of all odd integers
    range, the function returns 0.
    """
    sum_of_odd_ints = 0
    for i in range(639, 976):
        if integer_list[i] % 2 == 1:
            sum_of_odd_ints += integer_list[i]
    return sum_of_odd_ints