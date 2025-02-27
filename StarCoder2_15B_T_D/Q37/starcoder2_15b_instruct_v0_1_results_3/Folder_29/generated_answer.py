def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= '&' and char <= 'v' or (char < '&' or char > 'v'):
            filtered_string += char
    return filtered_string