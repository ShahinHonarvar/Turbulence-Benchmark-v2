def filter_chars(s):
    result = ''
    for index, char in enumerate(s):
        if index >= 1 and index <= 8 and ('8' < char < 'm'):
            continue
        result += char
    return result