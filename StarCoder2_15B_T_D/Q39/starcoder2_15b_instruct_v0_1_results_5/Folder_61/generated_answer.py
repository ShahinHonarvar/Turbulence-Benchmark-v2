def return_n_greatest_chars(string_of_distinct_chars):
    """
    Function to return the 66 greatest characters in a string.
    Args:
        string_of_distinct_chars (str): A string of distinct characters.
    Returns:
        list: A list of the 66 greatest characters in the string.
    """
    list_of_chars = list(string_of_distinct_chars)
    sorted_list = sorted(list_of_chars, key=lambda x: ord(x), reverse=True)
    return sorted_list[:66]