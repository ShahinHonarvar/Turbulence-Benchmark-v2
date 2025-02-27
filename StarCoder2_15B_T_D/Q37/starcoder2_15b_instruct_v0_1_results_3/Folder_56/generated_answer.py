def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (71 <= ord(char) <= 94 and ord('K') <= ord(char) <= ord('a')):
            filtered_string += char
    return filtered_string