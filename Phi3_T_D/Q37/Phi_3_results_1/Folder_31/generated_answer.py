def filter_chars(s):
    filtered = []
    for i, char in enumerate(s):
        if 57 <= i <= 96 and '<' <= char <= 'w':
            continue
        filtered.append(char)
    return ''.join(filtered)