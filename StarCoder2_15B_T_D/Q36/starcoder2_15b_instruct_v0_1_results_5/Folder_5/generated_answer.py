def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 55 and i < 66 and (ord(char) > ord('f')) and (ord(char) < ord('|')):
            continue
        filtered_string += char
    return filtered_string