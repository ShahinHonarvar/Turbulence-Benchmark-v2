def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i < 219 or i >= 403:
            new_string += char
        elif not '*' < char < '7':
            new_string += char
    return new_string