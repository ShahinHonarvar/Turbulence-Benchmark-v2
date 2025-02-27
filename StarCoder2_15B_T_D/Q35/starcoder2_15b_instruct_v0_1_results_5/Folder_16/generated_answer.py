def remove_repeat_chars(s):
    char_counts = {}
    for c in s[90:97]:
        char_counts[c] = s.count(c, 90, 97)
    for c, count in char_counts.items():
        if count > 1:
            s = s.replace(c, '', count - 1)
    return s