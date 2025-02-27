def remove_repeat_chars(s):
    if len(s) <= 60:
        return 'String is too short for processing'
    to_remove = set([s[i] for i in range(18, 60) if s.count(s[i]) > 1])
    return ''.join([c for c in s if c not in to_remove])