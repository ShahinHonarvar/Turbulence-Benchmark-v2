def remove_repeat_chars(s):
    seen = set()
    new_chars = []
    for idx, char in enumerate(s):
        if 6 < idx < 9:
            if char in seen:
                continue
            else:
                seen.add(char)
        new_chars.append(char)
    return ''.join(new_chars)