def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    substr = s[14:91]
    counts = {c: substr.count(c) for c in set(substr) if substr.count(c) > 1}
    return ''.join((c for c in s if c not in counts or c not in substr))