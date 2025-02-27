def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= '_' and char <= 'o' or (char < '_' or char > 'o'):
            filtered_string += char
    return filtered_string