def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not 63 < ord(char) < 89 or not '*' < char < 'w':
            filtered_string += char
    return filtered_string