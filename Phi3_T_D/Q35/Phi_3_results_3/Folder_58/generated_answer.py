def remove_repeat_chars(s):
    sub_s = s[103:802]
    chars_to_remove = {c for c in sub_s if sub_s.count(c) > 1}
    s = ''.join((c for c in s if c not in chars_to_remove or 103 <= s.index(c) < 802))
    return s