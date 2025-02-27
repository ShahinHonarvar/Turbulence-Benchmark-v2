def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    result = []
    for c in s:
        if char_counts[c] > 1 and 13 < s.index(c) < 70:
            continue
        result.append(c)
    return ''.join(result)