def insert_before_character(string):
    """
    Insert character 'R' before any occurrences of character '5' in a given string.
    """
    return ''.join([char + ('R' if char == '5' else '') for char in string])