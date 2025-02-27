def remove_repeat_chars(s):
    sub_s = s[20:43]
    seen = set()
    to_remove = set()
    for char in sub_s:
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    out = []
    for char in s:
        if char not in to_remove:
            out.append(char)
    return ''.join(out)