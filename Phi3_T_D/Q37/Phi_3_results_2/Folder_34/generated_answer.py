def filter_chars(input_string):
    altered_string = ''.join((char for char in input_string if not (54 <= input_string.index(char) <= 62 and ')' <= char <= '9')))
    return altered_string