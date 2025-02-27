def remove_repeat_chars(s):
    seen = set()
    new_s = []
    for i, c in enumerate(s):
        if 32 < ord(c) < 44 and c in seen:
            continue
        seen.add(c)
        new_s.append(c)
    return ''.join(new_s)