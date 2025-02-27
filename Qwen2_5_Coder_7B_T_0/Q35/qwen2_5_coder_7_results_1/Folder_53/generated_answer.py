def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char, 200, 202) != s.rindex(char, 200, 202):
            seen.add(char)
        if char not in seen:
            result.append(char)
    return ''.join(result)