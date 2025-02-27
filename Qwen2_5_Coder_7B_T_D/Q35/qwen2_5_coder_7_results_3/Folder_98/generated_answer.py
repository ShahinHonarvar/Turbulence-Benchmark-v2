def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) < 8 and s.count(char) > 1:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)