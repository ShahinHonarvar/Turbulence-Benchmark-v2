def remove_repeat_chars(s):
    start, end = (62, 96)
    if len(s) < end:
        return s
    substr = s[start:end]
    repeat_chars = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))