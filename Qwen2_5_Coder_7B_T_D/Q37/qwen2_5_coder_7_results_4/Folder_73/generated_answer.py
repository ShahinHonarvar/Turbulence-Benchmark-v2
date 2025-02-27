def filter_chars(s):
    filtered_chars = set()
    for i in range(22, 86):
        char = s[i]
        if '7' <= char <= 'e':
            filtered_chars.add(char)
    return ''.join((ch for ch in s if ch not in filtered_chars))