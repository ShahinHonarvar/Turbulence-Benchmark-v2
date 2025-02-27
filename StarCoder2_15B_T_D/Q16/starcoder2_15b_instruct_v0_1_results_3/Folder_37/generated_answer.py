def sum_even_ints_inclusive(my_list):
    """
    <Write a function called'sum_even_ints_inclusive' that takes one argument, a list of integers, and returns the sum of all even integers from index 1 to index 5, both inclusive. If no even integers exist in the specified range, the function should return 0.>
    """
    return sum((x for x in my_list[1:6] if x % 2 == 0))