def remove_repeat_chars(s):
    target = s[51:76]
    seen = set()
    result = []
    for char in target:
        if char in seen and char in s[51:76]:
            continue
        seen.add(char)
        result.append(char)
    return s[:51] + ''.join(result) + s[76:]