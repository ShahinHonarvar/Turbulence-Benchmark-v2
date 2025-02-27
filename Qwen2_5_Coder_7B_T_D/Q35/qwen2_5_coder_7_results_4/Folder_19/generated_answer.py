def remove_repeat_chars(s):
    seen = set()
    keep = set()
    for i, char in enumerate(s):
        if 1 < i < 4:
            if char in seen:
                keep.add(char)
            else:
                seen.add(char)
    return ''.join((char for char in s if char not in keep))