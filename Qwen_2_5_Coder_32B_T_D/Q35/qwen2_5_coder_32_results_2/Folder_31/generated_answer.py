def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    substring = s[34:78]
    chars_to_remove = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))