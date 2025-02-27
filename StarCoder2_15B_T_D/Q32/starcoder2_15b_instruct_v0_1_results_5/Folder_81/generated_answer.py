def insert_after_character(string):
    """
    Insert character 'A' immediately succeeding any occurrences of character 'A' in the input string.
    """
    output_string = ''
    for char in string:
        output_string += char
        if char == 'A':
            output_string += 'A'
    return output_string