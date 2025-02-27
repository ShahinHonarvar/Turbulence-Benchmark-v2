def remove_repeat_chars(s):
    chars_to_remove = set(s[3:9]) - {s[i] for i in range(3, 9) if s.count(s[i], 3, 9) == 1}
    return ''.join((c for c in s if c not in chars_to_remove))