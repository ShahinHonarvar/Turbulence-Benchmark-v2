def insert_after_character(string: str) -> str:
    """
    Insert character 'R' immediately succeeding any occurrences of character '5' in the given string.
    """
    return string.replace('5', '5R')