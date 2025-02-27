def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for char in s[0:8]:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return ''.join(result)