def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if i > 31 and i < 73 and ('M' < char < 'j'):
            continue
        result += char
    return result