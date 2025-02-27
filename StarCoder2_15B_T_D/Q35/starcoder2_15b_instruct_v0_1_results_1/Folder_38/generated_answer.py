def remove_repeat_chars(s):
    char_counts = {}
    chars_to_remove = set()
    for i, c in enumerate(s):
        if 36 < i < 85:
            char_counts[c] = char_counts.get(c, 0) + 1
            if char_counts[c] > 1:
                chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))