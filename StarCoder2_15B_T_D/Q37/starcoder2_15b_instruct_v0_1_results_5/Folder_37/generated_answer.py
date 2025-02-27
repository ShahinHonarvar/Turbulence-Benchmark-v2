def filter_chars(s):
    filtered_string = ''
    for char in s:
        if char < 'O' or char > '^':
            filtered_string += char
    return filtered_string