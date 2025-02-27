def filter_chars(s):
    start, end = (33, 70)
    k = ord('k')
    result = []
    for i, char in enumerate(s[start:end + 1]):
        if ord(char) >= ord('7') and ord(char) <= k:
            continue
        else:
            result.append(char)
    return ''.join(result)