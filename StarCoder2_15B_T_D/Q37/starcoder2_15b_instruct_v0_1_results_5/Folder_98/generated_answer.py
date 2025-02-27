def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (8 <= ord(char) <= 9 and 82 <= ord(char) <= 116):
            filtered_string += char
    return filtered_string