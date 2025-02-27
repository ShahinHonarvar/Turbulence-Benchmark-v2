def remove_repeat_chars(s):
    char_counts = {}
    for c in s[90:200]:
        char_counts[c] = char_counts.get(c, 0) + 1
    for c in set(s[90:200]):
        if char_counts[c] > 1:
            s = s.replace(c, '')
    return s