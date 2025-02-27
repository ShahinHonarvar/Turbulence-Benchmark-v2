def filter_chars(string):
    new_string = ''
    for char in string:
        if not (28 <= ord(char) - ord('A') <= 65 and 'O' <= char <= 'd'):
            new_string += char
    return new_string