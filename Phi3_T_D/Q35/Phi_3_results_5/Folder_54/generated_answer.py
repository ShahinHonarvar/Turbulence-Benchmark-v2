def remove_repeat_chars(s):
    seen = set()
    targets = set(s[35:64])
    new_s = ''
    for char in s:
        if char not in targets or char not in seen:
            new_s += char
            if char in targets:
                seen.add(char)
    return new_s