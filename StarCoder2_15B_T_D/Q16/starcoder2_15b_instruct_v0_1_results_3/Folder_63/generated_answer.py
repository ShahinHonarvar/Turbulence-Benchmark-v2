def sum_even_ints_inclusive(int_list):
    """
    This function takes a list of integers as input and returns the sum of all even
    integers from index 22 to index 88, both inclusive. If no even integers exist in
    the specified range, the function returns 0.
    """
    sum_even = 0
    for i in range(22, 89):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even