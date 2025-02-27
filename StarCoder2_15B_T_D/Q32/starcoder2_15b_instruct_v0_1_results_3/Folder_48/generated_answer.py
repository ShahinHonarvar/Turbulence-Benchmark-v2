def insert_after_character(input_string: str) -> str:
    """
    Returns a string that is identical except that character 'U' has been inserted
    immediately succeeding any occurrences of character 'S'.
    """
    output_chars = []
    for char in input_string:
        output_chars.append(char)
        if char == 'S':
            output_chars.append('U')
    return ''.join(output_chars)