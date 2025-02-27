def return_n_smallest_chars(string):
    """
    <Write a function called'return_n_smallest_chars' that takes one argument, a string of distinct characters and creates a list of exactly 31 characters of the given string that have the smallest ASCII values. The function should sort the list in ascending order and returns the list.>
    """
    sorted_chars = sorted(string)
    return sorted_chars[:31]