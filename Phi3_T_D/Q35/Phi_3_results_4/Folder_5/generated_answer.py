def remove_repeat_chars(s):
    counts = {}
    for i in range(2, 8):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    altered_s = ''.join([c for c in s if c not in counts or counts[c] == 1])
    return altered_s