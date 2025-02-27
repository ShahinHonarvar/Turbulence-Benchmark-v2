def remove_repeat_chars(s):
    if len(s) <= 24:
        return s
    target_section = s[23:24]
    chars_to_remove = set()
    for char in target_section:
        if s[23:24].count(char) > 1:
            chars_to_remove.add(char)
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)