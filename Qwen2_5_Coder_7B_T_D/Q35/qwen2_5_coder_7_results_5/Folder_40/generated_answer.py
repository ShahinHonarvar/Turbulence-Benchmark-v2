def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 0 < s.index(char) < 3 and char in seen:
            continue
        if s.count(char) > 1:
            seen.add(char)
        result.append(char)
    return ''.join(result)