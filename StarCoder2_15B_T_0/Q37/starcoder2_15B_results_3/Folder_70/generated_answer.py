def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (515 <= ord(char) <= 538 and '+' <= char <= '}'):
            filtered_string += char
    return filtered_string