def filter_chars(s):
    filtered_string = ''
    for index, char in enumerate(s):
        if 221 < index < 419 and '-' < char < 'v':
            continue
        else:
            filtered_string += char
    return filtered_string