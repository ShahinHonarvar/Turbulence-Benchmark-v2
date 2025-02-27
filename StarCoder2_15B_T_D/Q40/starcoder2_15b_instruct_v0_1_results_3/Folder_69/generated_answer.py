def return_n_smallest_chars(string):
    """
    This function takes a string of distinct characters and returns a list of the 65 characters
    with the smallest ASCII values, sorted in descending order.
    """
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.sort(key=ord)
    return char_list[:65][::-1]