def filter_chars(s):
    to_remove = set((s[i] for i in range(348, 853) if 'J' <= s[i] <= 'b'))
    return ''.join((c for c in s if c not in to_remove))