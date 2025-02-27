def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 1 < s.index(char) < 4 and char in seen:
            continue
        if 1 < s.index(char) < 4:
            seen.add(char)
        result.append(char)
    return ''.join(result)