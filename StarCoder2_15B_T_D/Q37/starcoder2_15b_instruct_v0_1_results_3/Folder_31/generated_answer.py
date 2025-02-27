def filter_chars(string):
    filtered_string = ''
    for char in string:
        if ord(char) < 57 or ord(char) > 96 or char < '<' or (char > 'w'):
            filtered_string += char
    return filtered_string