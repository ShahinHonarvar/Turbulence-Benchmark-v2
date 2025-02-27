def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for i in range(10, 79):
        if s[i] in seen:
            repeat.add(s[i])
        seen.add(s[i])
    return ''.join((c for c in s if c not in repeat))