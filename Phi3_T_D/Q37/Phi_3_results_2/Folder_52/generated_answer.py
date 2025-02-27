def filter_chars(s):
    modified_string = ''
    for i, char in enumerate(s):
        if 54 <= i <= 83 and 'j' <= char <= 'v':
            continue
        modified_string += char
    return modified_string