def remove_repeat_chars(s):
    counts = {}
    for i in range(48, 76):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([c for c in s if counts[c] <= 1 or c not in range(48, 76)])