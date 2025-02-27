def filter_chars(s):
    result = ''
    for char in range(11, 73):
        char = s[char]
        if 'i' <= char <= 'v':
            continue
        result += char
    return result