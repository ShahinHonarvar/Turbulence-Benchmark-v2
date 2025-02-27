def remove_repeat_chars(s):
    if len(s) <= 989:
        return s
    section = s[356:988]
    counts = {}
    for char in section:
        counts[char] = counts.get(char, 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))