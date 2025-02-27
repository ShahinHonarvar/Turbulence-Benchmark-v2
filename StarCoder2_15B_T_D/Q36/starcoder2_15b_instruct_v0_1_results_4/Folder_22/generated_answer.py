def filter_chars(string):
    char_set = set(string[55:84])
    filtered_chars = [char for char in string if not (char > ';' and char < 'z')]
    return ''.join(filtered_chars)