def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (35 <= ord(char) - ord('0') <= 51 and ord('H') <= ord(char) <= ord('s')):
            filtered_string += char
    return filtered_string