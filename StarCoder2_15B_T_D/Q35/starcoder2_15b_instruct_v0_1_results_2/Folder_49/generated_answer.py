def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    repeat_chars = [c for c in char_counts if 90 < char_counts[c] < 200]
    return ''.join((c for c in s if c not in repeat_chars))