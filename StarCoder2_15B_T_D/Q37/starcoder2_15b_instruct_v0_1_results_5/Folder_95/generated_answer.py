def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < ')' or char > 'l' or string.index(char) < 35 or (string.index(char) > 40):
            filtered_string += char
    return filtered_string