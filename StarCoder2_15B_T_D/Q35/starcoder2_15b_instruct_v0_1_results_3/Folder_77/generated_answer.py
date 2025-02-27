def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    repeated_chars = [c for c in char_counts if char_counts[c] > 1]
    for c in repeated_chars:
        s = s.replace(c, '')
    return s