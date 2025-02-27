def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 38 < i < 81 and '.' < char < '^':
            continue
        else:
            result.append(char)
    return ''.join(result)