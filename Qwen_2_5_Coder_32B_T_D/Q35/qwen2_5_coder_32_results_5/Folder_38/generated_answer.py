def remove_repeat_chars(s):
    if len(s) <= 85:
        return s
    target_section = s[37:85]
    char_count = {c: target_section.count(c) for c in target_section}
    chars_to_remove = {c for c, count in char_count.items() if count > 1}
    return ''.join((c for c in s if c not in chars_to_remove))