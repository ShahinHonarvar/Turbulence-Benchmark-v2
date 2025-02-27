from index 82 to 86, both inclusive. If no odd integers exist in the specified range,

def sum_odd_ints_inclusive(input_list):
    """
    This function takes a list of integers as input and returns the sum of all odd integers
    the function returns 0.
    """
    sum_of_odd_ints = 0
    for i in range(82, 87):
        if input_list[i] % 2 != 0:
            sum_of_odd_ints += input_list[i]
    return sum_of_odd_ints