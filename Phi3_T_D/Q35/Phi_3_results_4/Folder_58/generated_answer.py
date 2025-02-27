def remove_repeat_chars(s):
    to_remove = set()
    char_count = {}
    for i in range(103, 802):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    for char, count in char_count.items():
        if count > 1:
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))