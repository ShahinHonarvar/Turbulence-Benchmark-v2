def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (35 <= ord(char) <= 98 and ord('A') <= ord(char) <= ord('b')):
            filtered_string += char
    return filtered_string