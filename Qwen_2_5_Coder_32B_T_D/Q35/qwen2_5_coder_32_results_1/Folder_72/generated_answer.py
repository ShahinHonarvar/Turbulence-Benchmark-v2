def remove_repeat_chars(s):
    if len(s) <= 71:
        return s
    segment = s[14:70]
    char_count = {char: segment.count(char) for char in segment if segment.count(char) > 1}
    return ''.join([char for char in s if char not in char_count])