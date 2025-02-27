def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(1, 6):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            result = [c for c in result if c != s[i]]
    return ''.join(result)