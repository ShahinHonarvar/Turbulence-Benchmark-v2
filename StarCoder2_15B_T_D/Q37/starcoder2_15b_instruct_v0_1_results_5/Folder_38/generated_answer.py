def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= 'a' and char <= 'f':
            if string.index(char) < 24 or string.index(char) > 79:
                filtered_string += char
    return filtered_string