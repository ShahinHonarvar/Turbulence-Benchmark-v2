def filter_chars(input_string):
    filtered_string = [char for char in input_string if (char < '\\x21' or char > '\\x5A') or not '\\x27' <= char <= '\\x7B']
    return ''.join(filtered_string)