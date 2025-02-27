def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if (i >= 343 and i < 665) and '%' < char < 'U':
            continue
        filtered_string += char
    return filtered_string