def remove_repeat_chars(s):
    if len(s) < 98:
        return s
    section = s[70:97]
    repeat_chars = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))