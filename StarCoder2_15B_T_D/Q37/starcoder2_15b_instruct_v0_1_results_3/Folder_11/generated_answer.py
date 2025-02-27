def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not 29 <= ord(char) - ord('-') <= 68:
            filtered_string += char
    return filtered_string