def remove_repeat_chars(s):
    chars_to_remove = set(s[409:502]) - {s[i] for i in range(max(409, 0), 503) if s[i - 409] != s[i]}
    return ''.join((c for c in s if c not in chars_to_remove or c[409:502].count(c) == 1))