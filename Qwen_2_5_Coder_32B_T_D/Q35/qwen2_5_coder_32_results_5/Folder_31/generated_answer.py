def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    segment = s[34:78]
    char_count = {c: segment.count(c) for c in set(segment) if segment.count(c) > 1}
    return ''.join((c for c in s if c not in char_count))