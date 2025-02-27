def sum_even_ints_inclusive(integer_list):
    """
    Write a function called'sum_even_ints_inclusive' that takes one argument,
    a list of integers, and returns the sum of all even integers from index 10
    to index 66, both inclusive. If no even integers exist in the specified
    range, the function should return 0.
    """
    sum_even_ints = 0
    for i in range(10, 67):
        if integer_list[i] % 2 == 0:
            sum_even_ints += integer_list[i]
    return sum_even_ints