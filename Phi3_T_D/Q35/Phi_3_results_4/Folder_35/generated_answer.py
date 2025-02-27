def remove_repeat_chars(s):
    repeats = set((s[i] for i in range(78, 83) if s[i - 1] == s[i] == s[i + 1]))
    return ''.join((c for c in s if c not in repeats or (78 <= s.index(c) <= 83 and repeats.add(c))))