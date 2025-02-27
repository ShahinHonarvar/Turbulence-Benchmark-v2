def insert_before_character(string):
    """
    Insert character '0' before any occurrences of character 'e' in a string.
    """
    return ''.join([c if c != 'e' else '0e' for c in string])