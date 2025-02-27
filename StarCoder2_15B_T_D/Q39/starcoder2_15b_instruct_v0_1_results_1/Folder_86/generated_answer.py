def return_n_greatest_chars(string):
    """
    This function takes a string of distinct characters and returns the sorted list of exactly 34 characters of the given string that have the greatest ASCII values.
    """
    sorted_string = sorted(string, reverse=True)
    return sorted_string[:34]