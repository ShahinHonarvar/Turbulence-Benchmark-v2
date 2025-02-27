def remove_repeat_chars(s):
    seen = set()
    new_str = []
    for i in range(3):
        char = s[i]
        if char not in seen:
            new_str.append(char)
            seen.add(char)
    if s[3] != s[2]:
        new_str.append(s[3])
    return ''.join(new_str)