def remove_repeat_chars(s):
    unique_chars = set(s[20:200])
    filtered_string = ''.join((c for i, c in enumerate(s) if c not in unique_chars or s.find(c, i + 1) not in range(20, 200)))
    return filtered_string