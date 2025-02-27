def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i > 60 and i < 88 and ('%' < char < 'q'):
            filtered_string += char
    return filtered_string