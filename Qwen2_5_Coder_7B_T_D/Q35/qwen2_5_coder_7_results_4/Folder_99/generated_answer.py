def remove_repeat_chars(s):
    counts = {}
    for i in range(451, 905):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([c for c in s if counts[c] <= 1 or i <= 450 or i >= 905])