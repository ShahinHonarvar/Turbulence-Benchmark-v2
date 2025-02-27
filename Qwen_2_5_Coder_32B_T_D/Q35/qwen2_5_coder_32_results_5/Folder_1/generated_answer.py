def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    target_section = s[18:88]
    char_count = {char: target_section.count(char) for char in target_section if target_section.count(char) > 1}
    result = [c for c in s if c not in char_count]
    return ''.join(result)