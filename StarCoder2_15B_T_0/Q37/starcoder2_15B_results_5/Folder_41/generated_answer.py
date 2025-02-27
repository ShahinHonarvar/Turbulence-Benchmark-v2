def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (26 <= ord(char) - ord('A') <= 64 and 'V' <= char <= 'o'):
            filtered_string += char
    return filtered_string