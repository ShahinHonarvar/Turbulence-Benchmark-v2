def remove_repeat_chars(s):
    indices = range(450, 905)
    char_indexes = {c: [] for c in set(s) if 450 < s.index(c) < len(s) - 555}
    for i in indices:
        if s[i] in char_indexes:
            char_indexes[s[i]].append(i)
    chars_to_remove = {c for c, indexes in char_indexes.items() if len(indexes) > 1}
    return ''.join([c for c, i in zip(s, indices) if c not in chars_to_remove or i not in char_indexes[c]])