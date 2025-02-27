def insert_before_character(input_string):
    """
    Insert 'P' immediately preceding any occurrences of 'C' in the input string.
    """
    output_string = ''
    for char in input_string:
        if char == 'C':
            output_string += 'PC'
        else:
            output_string += char
    return output_string