def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(68, 99):
        char = s[i]
        if char not in seen and s.count(char, i) > 1:
            seen.add(char)
        else:
            continue
        result.append(char)
    return ''.join(result) if len(result) < len(s) else s[68:99]