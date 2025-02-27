def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 26 < i < 80 and '<' < char < '>':
            continue
        result.append(char)
    return ''.join(result)