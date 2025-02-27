def remove_repeat_chars(s):
    to_remove = {ch for ch in s[86:90] if s[86:90].count(ch) > 1}
    return ''.join((ch for ch in s if ch not in to_remove))