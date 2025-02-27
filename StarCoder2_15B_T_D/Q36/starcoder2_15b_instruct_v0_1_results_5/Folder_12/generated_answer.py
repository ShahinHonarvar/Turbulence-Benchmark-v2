def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 32 < ord(char) < 84 and char > 'm' and (char < 'w'):
            filtered_string += char
    return filtered_string