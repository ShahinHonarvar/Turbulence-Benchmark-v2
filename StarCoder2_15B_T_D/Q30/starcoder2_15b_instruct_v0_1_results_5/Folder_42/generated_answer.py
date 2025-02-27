def insert_before_character(string):
    """
    Insert character 'j' before any occurrences of character 'O' in the given string.
    """
    output = []
    for char in string:
        if char == 'O':
            output.append('j')
        output.append(char)
    return ''.join(output)