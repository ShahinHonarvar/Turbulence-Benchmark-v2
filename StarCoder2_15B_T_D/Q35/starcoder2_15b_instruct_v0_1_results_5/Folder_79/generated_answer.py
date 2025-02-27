def remove_repeat_chars(s):
    char_counts = {}
    for c in s[1:7]:
        char_counts[c] = char_counts.get(c, 0) + 1
    repeated_chars = {c for c, count in char_counts.items() if count > 1}
    filtered_chars = [c for c in s if c not in repeated_chars]
    return ''.join(filtered_chars)