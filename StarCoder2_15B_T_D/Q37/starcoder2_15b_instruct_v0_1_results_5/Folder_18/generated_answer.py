def filter_chars(string):
    filtered_string = ''
    for char in string:
        if string.index(char) < 770 or string.index(char) > 970 or char < '-' or (char > 'D'):
            filtered_string += char
    return filtered_string