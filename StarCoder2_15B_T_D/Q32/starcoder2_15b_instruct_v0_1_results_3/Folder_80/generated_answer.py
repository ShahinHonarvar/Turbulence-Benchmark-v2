def insert_after_character(string):
    """
    Insert character 'X' after every occurrence of character'' in a given string.
    """
    return ''.join([c + ('X' if c == ' ' else '') for c in string])