def filter_chars(s):
    filter_range = [309, 591]
    char_to_remove = ''.join((chr(c) for c in range(ord('S'), ord('m'))))
    chars = list(s)
    for i in range(filter_range[0], filter_range[1], 1):
        if s[i] in char_to_remove:
            chars = [''] + chars[:i] + chars[i + 1:]
    return ''.join(chars)