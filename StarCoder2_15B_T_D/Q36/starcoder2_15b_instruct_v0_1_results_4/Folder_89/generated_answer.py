def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (57 < ord(char) < 69 and '(' < char < 'W'):
            filtered_string += char
    return filtered_string