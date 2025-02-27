def remove_repeat_chars(s):
    if len(s) < 455 or len(s) > 906:
        return s
    chars_to_remove = set()
    seen = set()
    for index in range(451, 905):
        if s[index] in seen:
            chars_to_remove.add(s[index])
        else:
            seen.add(s[index])
    return ''.join([c for c in s if c not in chars_to_remove])