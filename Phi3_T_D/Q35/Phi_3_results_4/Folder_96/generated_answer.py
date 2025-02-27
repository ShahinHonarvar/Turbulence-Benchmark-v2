def remove_repeat_chars(s):
    chars_to_remove = set(s[60:200]) - {s[60:200].count(c) == 1 for c in s[60:200]}
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 60 or s.index(c) >= 200))