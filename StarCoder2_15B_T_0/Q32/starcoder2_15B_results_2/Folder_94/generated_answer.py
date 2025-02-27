def insert_after_character(string):
    """
    Insert character '5' after any occurrences of character'' in the given string.
    """
    return ''.join([c + ('5' if c == '' else '') for c in string])