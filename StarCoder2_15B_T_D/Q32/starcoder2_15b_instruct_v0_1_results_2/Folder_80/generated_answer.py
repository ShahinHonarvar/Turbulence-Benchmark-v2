def insert_after_character(input_string):
    """
    Insert character 'X' immediately succeeding any occurrences of character''.

    Args:
        input_string (str): Input string.

    Returns:
        str: String with character 'X' inserted immediately succeeding any occurrences of character''.
    """
    output_string = ''
    for char in input_string:
        output_string += char
        if char == '':
            output_string += 'X'
    return output_string