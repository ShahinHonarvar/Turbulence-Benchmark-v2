def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < '7' or char > 'k' or (char < '7' and char > 'k'):
            filtered_string += char
    return filtered_string