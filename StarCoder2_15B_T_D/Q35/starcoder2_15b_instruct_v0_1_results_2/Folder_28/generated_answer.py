def remove_repeat_chars(s):
    counts = {}
    for c in s[86:99]:
        counts[c] = counts.get(c, 0) + 1
    repeated_chars = {c for c, count in counts.items() if count > 1}
    result = []
    for c in s:
        if c not in repeated_chars:
            result.append(c)
    return ''.join(result)