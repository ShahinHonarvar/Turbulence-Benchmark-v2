def remove_repeat_chars(s):
    counts = [0] * 256
    for i in range(16, 87):
        counts[ord(s[i])] += 1
    keep = [counts[ord(c)] == 0 for c in s]
    return ''.join((c for c, k in zip(s, keep) if k))