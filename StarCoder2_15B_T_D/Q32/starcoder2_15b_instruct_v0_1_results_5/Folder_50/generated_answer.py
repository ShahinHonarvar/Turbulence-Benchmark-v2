def insert_after_character(string):
    """
    Insert 'u' after 't' in a given string.

    Parameters:
    string (str): The input string.

    Returns:
    str: The modified string with 'u' inserted after 't'.
    """
    return ''.join([c + ('u' if c == 't' else '') for c in string])