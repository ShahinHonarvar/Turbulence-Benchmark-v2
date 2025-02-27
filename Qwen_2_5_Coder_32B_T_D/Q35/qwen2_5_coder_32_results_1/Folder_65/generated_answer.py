def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    target_section = s[52:76]
    char_count = {char: target_section.count(char) for char in set(target_section) if target_section.count(char) > 1}
    return ''.join((char for char in s if char not in char_count))