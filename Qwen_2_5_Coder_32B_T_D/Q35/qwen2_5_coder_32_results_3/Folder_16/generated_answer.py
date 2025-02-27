def remove_repeat_chars(s):
    if len(s) <= 97:
        return s
    target_section = s[91:97]
    chars_to_remove = set([char for char in target_section if target_section.count(char) > 1])
    return ''.join([char for char in s if char not in chars_to_remove])