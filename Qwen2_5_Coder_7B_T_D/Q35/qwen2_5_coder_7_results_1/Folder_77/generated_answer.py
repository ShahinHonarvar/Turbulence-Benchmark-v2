def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s[:355] + s[988:]:
        if char in seen:
            if char not in s[355:988]:
                result.append(char)
        else:
            seen.add(char)
            result.append(char)
    return ''.join(result)