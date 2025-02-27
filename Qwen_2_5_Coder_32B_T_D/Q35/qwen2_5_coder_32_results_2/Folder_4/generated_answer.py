def remove_repeat_chars(s):
    t = s[50:74]
    count = {ch: t.count(ch) for ch in set(t)}
    chars_to_remove = {ch for ch, c in count.items() if c > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove))