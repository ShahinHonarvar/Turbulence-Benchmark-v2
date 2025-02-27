def insert_before_character(string):
    """
    Insert 'U' before every occurrence of 'S' in the given string.
    """
    return ''.join([c if c != 'S' else 'US' for c in string])