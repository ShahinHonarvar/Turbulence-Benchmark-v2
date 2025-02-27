def insert_before_character(string):
    """
    Insert the character 'E' immediately preceding any occurrences of character 'e' in a string.
    """
    return ''.join([c if c != 'e' else 'Ee' for c in string])