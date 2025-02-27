def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if (i >= 39 and i < 87) and (ord(char) > ord('!') and ord(char) < ord('}')):
            filtered_string += char
    return filtered_string