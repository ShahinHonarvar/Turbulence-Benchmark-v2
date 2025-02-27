def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub = s[38:43]
    char_count = {char: sub.count(char) for char in sub}
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))