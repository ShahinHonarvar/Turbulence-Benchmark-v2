def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    new_chars = set()
    new_string = ''
    for c in s:
        if c not in new_chars and char_counts[c] > 1 and (29 < s.index(c) < 53):
            new_chars.add(c)
            new_string += c
    return new_string