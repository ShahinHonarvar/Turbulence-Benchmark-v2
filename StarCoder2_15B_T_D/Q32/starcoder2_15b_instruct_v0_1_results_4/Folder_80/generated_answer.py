def insert_after_character(string):
    """
    Insert 'X' after every occurrence of'' in the given string.
    """
    result = ''
    for character in string:
        result += character
        if character == ' ':
            result += 'X'
    return result