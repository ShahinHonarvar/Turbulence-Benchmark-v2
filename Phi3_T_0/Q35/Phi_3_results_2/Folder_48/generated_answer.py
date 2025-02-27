def remove_repeat_chars(s):
    start, end = (409, 502)
    seen = set()
    result = []
    for i in range(len(s)):
        if start <= i < end:
            if s[i] in seen:
                continue
            seen.add(s[i])
        result.append(s[i])
    return ''.join(result)