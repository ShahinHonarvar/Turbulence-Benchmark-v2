def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 200 < s.index(char) < 202:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)