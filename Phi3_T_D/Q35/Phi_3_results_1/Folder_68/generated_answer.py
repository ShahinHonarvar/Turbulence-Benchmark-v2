def remove_repeat_chars(s):
    seen = set()
    return ''.join((c for i, c in enumerate(s) if i < 10 and c not in seen or seen.add(c)))