def insert_after_character(string):
    """
    Insert character '9' after character '6' in a given string.
    """
    return ''.join([c + ('9' if c == '6' else '') for c in string])