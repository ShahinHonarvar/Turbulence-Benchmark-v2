def remove_repeat_chars(s):
    target_chars = {ch for ch in s[3:8] if s.count(ch) > 1}
    return ''.join((ch for ch in s if not (ch in target_chars and 3 <= s.index(ch) < 8)))