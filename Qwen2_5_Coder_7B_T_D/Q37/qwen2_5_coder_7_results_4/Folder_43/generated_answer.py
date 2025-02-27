def filter_chars(s):
    return ''.join((c for c in s if not (15 <= s.find(c) <= 55 and 'W' <= c <= '{') and c not in s[s.find(c) + 1:]))