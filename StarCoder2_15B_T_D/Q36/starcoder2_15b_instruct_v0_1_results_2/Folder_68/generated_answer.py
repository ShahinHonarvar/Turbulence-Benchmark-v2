def filter_chars(string):
    new_string = ''
    for char in string:
        if not (char.isalpha() and '8' < char < 'm'):
            new_string += char
    return new_string