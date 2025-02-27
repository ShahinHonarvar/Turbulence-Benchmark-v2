def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 0 < s.index(char) < 8 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)