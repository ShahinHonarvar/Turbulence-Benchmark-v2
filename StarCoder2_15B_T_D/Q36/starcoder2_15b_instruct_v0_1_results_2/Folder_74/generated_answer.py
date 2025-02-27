def filter_chars(string):
    new_string = ''
    for char in string:
        if not (33 < ord(char) < 36 and '>' < char < 'A'):
            new_string += char
    return new_string