def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    chars = set(s[21:35])
    count = {char: s[21:35].count(char) for char in chars if s[21:35].count(char) > 1}
    return ''.join((char for char in s if char not in count))