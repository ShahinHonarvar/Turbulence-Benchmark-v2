def remove_repeat_chars(s):
    target_range = s[44:91]
    seen = set()
    for char in target_range:
        if target_range.count(char) > 1:
            s = s.replace(char, '')
    return s