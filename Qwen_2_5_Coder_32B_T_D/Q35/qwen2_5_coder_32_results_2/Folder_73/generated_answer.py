def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    target_section = s[10:76]
    chars_to_remove = {char for char in target_section if target_section.count(char) > 1}
    return ''.join([char for char in s if char not in chars_to_remove])