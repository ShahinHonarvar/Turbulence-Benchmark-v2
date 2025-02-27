def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s[0:8]):
        if char not in seen_chars:
            result.append(char)
            seen_chars.add(char)
    return ''.join(result) + s[8:]