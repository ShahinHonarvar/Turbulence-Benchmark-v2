def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 24 and i < 37 and (not (ord(char) > ord('A') and ord(char) < ord('h'))):
            filtered_string += char
    return filtered_string