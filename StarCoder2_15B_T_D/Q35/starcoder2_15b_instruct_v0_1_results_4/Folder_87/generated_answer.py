def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    return ''.join((c for c in s if char_counts[c] == 1 or s.index(c) < 20 or s.index(c) >= 43))