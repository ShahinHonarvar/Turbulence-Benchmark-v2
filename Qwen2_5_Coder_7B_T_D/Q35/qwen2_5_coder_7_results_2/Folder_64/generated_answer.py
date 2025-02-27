def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) > 5 or char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)