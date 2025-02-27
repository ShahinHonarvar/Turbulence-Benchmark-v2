def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char, 0, 4) != s.rindex(char, 0, 4):
            seen.add(char)
        if char not in seen:
            result.append(char)
    return ''.join(result)