def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 61 < ord(char) < ord('q') and 61 < i < 88:
            continue
        else:
            result.append(char)
    return ''.join(result)