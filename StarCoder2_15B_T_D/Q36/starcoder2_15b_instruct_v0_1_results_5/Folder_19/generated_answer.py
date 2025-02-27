def filter_chars(input_string):
    output_string = ''
    for char in input_string:
        if not (77 < ord(char) < 87 and ';' < char < 'r'):
            output_string += char
    return output_string