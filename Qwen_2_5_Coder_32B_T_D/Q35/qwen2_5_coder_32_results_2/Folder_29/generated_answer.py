def remove_repeat_chars(s):
    if len(s) <= 98:
        return s
    substr = s[71:98]
    repeat_chars = {c for c in substr if substr.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))