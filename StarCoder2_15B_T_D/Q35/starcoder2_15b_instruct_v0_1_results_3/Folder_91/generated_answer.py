def remove_repeat_chars(s):
    char_counts = {}
    for c in s[:6]:
        char_counts[c] = char_counts.get(c, 0) + 1
    repeat_chars = {c for c, count in char_counts.items() if count > 1}
    new_string = ''
    for c in s:
        if c not in repeat_chars:
            new_string += c
    return new_string