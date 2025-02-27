def filter_chars(s):
    modified_string = ''
    for index, char in enumerate(s):
        if 18 < index < 95 and 'K' < char < 'a':
            continue
        modified_string += char
    return modified_string