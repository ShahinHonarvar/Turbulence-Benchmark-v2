def filter_chars(text):
    chars = list(text)
    for i in range(40, 63):
        if chars[i] > '7' and chars[i] < 'H':
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)