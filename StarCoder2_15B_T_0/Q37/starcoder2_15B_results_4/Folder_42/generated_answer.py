def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (73 <= ord(char) <= 74 and ord('U') <= ord(char) <= ord('l')):
            filtered_string += char
    return filtered_string