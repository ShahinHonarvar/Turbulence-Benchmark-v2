def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= '-' and char <= 'n' or (char < '-' or char > 'n'):
            filtered_string += char
    return filtered_string