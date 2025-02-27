def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (57 <= ord(char) <= 96 and char.isprintable() and char.isalpha() and (char.lower() <= 'w')):
            filtered_string += char
    return filtered_string