def remove_repeat_chars(s):
    target_chars = {s[i] for i in range(201, 202) if s.count(s[i]) > 1}
    return ''.join((ch for ch in s if ch not in target_chars))