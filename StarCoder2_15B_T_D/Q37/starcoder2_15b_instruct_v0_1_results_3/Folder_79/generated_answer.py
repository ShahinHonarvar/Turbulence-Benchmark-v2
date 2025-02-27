def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not 10 <= ord(char) - ord('@') <= 42:
            filtered_string += char
    return filtered_string