def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not 61 <= ord(char) <= 70:
            filtered_string += char
    return filtered_string