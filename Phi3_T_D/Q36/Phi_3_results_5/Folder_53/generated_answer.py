def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i > 90 and i < 97 and (char > 'j') and (char < 'w'):
            continue
        result.append(char)
    return ''.join(result)