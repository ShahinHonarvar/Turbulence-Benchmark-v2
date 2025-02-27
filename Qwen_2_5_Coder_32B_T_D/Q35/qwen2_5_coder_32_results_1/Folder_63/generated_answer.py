def remove_repeat_chars(s):
    if len(s) <= 86:
        return s
    substr = s[82:86]
    chars_to_remove = {c for c in substr if substr.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))