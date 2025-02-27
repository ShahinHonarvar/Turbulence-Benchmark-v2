def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    target_section = s[51:92]
    repeat_chars = {char for char in target_section if target_section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))