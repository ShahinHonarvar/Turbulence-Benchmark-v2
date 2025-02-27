def remove_repeat_chars(s):
    seen = {}
    result = []
    for char in s:
        if s.index(char) < 3 and char not in seen:
            seen[char] = True
            result.append(char)
    return ''.join(result)