def remove_repeat_chars(s):
    if len(s) <= 96:
        return s
    substr = s[28:96]
    char_count = {char: substr.count(char) for char in substr}
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))