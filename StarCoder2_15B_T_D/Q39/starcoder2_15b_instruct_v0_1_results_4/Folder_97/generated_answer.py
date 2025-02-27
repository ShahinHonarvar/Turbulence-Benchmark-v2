def return_n_greatest_chars(input_string):
    """
    Returns a sorted list of exactly 38 characters of the given string that have the greatest ASCII values.
    """
    char_dict = {}
    for char in input_string:
        char_dict[char] = ord(char)
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict[:38]