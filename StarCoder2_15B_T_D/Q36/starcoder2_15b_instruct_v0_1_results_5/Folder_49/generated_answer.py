def filter_chars(string):
    new_string = ''
    for char in string:
        if not (46 < ord(char) < 91 and 'D' < char < 'H'):
            new_string += char
    return new_string