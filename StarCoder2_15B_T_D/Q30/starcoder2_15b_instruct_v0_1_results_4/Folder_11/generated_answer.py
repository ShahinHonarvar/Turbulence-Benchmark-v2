def insert_before_character(string):
    """
    Insert character 't' before any occurrences of character 'g' in the given string.
    """
    return ''.join([c if c != 'g' else 'tg' for c in string])