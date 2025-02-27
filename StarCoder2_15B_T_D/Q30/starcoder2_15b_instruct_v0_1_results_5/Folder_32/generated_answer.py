def insert_before_character(input_string):
    """
    Insert character 'u' immediately preceding any occurrences of character 'F'.
    """
    output_string = ''
    for char in input_string:
        if char == 'F':
            output_string += 'u'
        output_string += char
    return output_string