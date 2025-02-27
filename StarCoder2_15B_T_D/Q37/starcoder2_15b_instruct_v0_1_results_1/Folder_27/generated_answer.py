def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (43 <= ord(char) <= 80 and '=' <= char <= 'E'):
            filtered_string += char
    return filtered_string