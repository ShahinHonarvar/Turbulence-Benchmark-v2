def remove_repeat_chars(s):
    start, end = (43, 71)
    seen = set()
    result = []
    for i, char in enumerate(s[start:end]):
        if char not in seen:
            seen.add(char)
            result.append(char)
    return s[:start] + ''.join(result) + s[end:]