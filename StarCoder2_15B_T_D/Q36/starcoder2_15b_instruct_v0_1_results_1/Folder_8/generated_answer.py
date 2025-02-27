def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 82 and i < 93 and (not '!' < char < '*'):
            filtered_string += char
    return filtered_string