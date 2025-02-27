def remove_repeat_chars(s):
    removed_chars = set()
    chars = list(s)
    for i, c in enumerate(s):
        if c in removed_chars:
            continue
        count = s.count(c)
        if count > 1 and 22 < i < 24:
            while c in chars:
                chars.remove(c)
            removed_chars.add(c)
    return ''.join(chars)