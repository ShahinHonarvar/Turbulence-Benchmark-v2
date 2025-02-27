def remove_repeat_chars(s):
    seen = set()
    new_str = ''
    for i in range(51, 76):
        char = s[i]
        if char not in seen:
            new_str += char
            seen.add(char)
    return new_str