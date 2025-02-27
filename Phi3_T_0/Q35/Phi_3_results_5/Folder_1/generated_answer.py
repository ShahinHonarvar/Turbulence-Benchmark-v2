def remove_repeat_chars(s):
    start, end = (17, 88)
    seen = set()
    result = []
    for i, char in enumerate(s[start:end]):
        if char not in seen:
            seen.add(char)
        else:
            s = s[:start + i] + s[start + i + 1:]
            seen.remove(char)
            i -= 1
    return s[:start] + ''.join(result) + s[end:]