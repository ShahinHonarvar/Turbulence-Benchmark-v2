def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(51, 76):
        char = s[i]
        if char in seen:
            continue
        if s.count(char, 51, 76) > 1:
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result[:51] + s[76:])