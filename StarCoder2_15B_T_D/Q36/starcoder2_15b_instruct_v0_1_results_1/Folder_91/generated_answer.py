def filter_chars(string):
    char_to_remove = string[1:3]
    new_string = ''
    for char in string:
        if char not in char_to_remove:
            new_string += char
    return new_string