def all_even_ints_inclusive(num_list):
    """Returns the list of all even integers from index 35 to index 49, both inclusive. If no even integers exist in the specified range, returns an empty list."""
    return [num for i, num in enumerate(num_list) if i >= 35 and i <= 49 and (num % 2 == 0)]