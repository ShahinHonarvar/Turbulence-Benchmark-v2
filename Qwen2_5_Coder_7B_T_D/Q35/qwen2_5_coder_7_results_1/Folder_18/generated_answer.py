def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 56 < s.index(char) < 90:
            if char not in seen:
                seen.add(char)
                result.append(char)
    return ''.join(result)