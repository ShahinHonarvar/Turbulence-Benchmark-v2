def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not 7 <= ord(char) - ord('A') <= 8:
            filtered_string += char
    return filtered_string