def filter_chars(s):
    filtered = []
    for index, char in enumerate(s[36:80]):
        if '2' <= char <= 's':
            continue
        filtered.append(char)
    return s[:36] + ''.join(filtered) + s[80:]