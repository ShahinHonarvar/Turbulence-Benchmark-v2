def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i >= 37 and i < 43:
            char_counts[c] = char_counts.get(c, 0) + 1
    removed_chars = set()
    result = ''
    for c in s:
        if c not in removed_chars and char_counts.get(c, 0) > 1:
            removed_chars.add(c)
        else:
            result += c
    return result