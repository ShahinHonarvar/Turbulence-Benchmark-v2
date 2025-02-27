def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 37 or i > 56 or ord(char) < 54 or (ord(char) > 95):
            filtered_string += char
    return filtered_string