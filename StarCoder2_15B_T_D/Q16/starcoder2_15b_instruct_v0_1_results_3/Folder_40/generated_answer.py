def sum_even_ints_inclusive(lst):
    """
    sum_even_ints_inclusive takes one argument, a list of integers, and returns the sum of all even integers from index 0 to index 2, both inclusive. If no even integers exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(3):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum