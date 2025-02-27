def insert_after_character(string):
    """
    Insert character 'a' after any occurrences of character 'A' in a string.
    """
    output = ''
    for character in string:
        if character == 'A':
            output += 'Aa'
        else:
            output += character
    return output