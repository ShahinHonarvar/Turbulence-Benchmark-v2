def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 68 < s.index(char) < 99 and char in seen:
            continue
        elif 68 < s.index(char) < 99:
            seen.add(char)
        result.append(char)
    return ''.join(result)