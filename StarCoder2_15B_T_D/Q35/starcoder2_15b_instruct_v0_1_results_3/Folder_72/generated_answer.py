def remove_repeat_chars(s):
    counts = {}
    for c in s[13:70]:
        counts[c] = counts.get(c, 0) + 1
    new_s = ''
    for c in s:
        if counts[c] == 1 or c not in counts:
            new_s += c
    return new_s