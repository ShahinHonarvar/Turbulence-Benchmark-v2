def filter_chars(string):
    filtered_string = ''
    for char in string:
        if (char >= 'a' and char <= 'f') and (string.index(char) >= 24 and string.index(char) <= 79):
            continue
        else:
            filtered_string += char
    return filtered_string