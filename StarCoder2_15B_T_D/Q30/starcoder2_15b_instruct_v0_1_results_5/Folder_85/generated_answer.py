def insert_before_character(string):
    """
    Insert character 'a' before any occurrences of character 'o' in the given string.
    """
    return ''.join([c if c != 'o' else 'ao' for c in string])