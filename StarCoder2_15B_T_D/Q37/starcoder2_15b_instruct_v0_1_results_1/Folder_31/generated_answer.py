def filter_chars(string):
    filtered_string = ''
    for char in string:
        if (char < '<' or char > 'w') or (ord(char) < 57 or ord(char) > 96):
            filtered_string += char
    return filtered_string