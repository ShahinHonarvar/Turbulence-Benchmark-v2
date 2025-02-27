def insert_before_character(string):
    """
    Insert character 'I' before any occurrences of character 'i' in the given string.
    """
    return string.replace('i', 'Ii').replace('I', 'I')