def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(39, 43):
        char = s[i]
        if char not in seen:
            seen.add(char)
        else:
            result = ''.join([c for c in result if c != char])
    return ''.join(result)