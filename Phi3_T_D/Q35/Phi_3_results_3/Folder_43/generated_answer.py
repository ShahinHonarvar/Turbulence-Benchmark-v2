def remove_repeat_chars(s):
    unique_chars = []
    for i, c in enumerate(s[10:27], start=10):
        if c not in s[i:27] and c not in unique_chars:
            unique_chars.append(c)
    return ''.join((c for c in s if c in unique_chars))