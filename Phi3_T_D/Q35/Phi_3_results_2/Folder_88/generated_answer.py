def remove_repeat_chars(s):
    freq = {}
    for i in range(3, 9):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    return ''.join([c for i, c in enumerate(s) if c not in freq or s[i:i + 9].count(c) == 1])