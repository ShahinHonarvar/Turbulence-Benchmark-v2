def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s[1:6]:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)