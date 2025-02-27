def remove_repeat_chars(s):
    if len(s) <= 8:
        return s
    target_section = s[1:8]
    repeat_chars = {char for char in target_section if target_section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))