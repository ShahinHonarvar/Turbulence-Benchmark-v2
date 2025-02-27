def remove_repeat_chars(s):
    seen, result = (set(), '')
    for char in s:
        if ord(char) >= 90 and ord(char) < 97:
            if char not in seen:
                seen.add(char)
                result += char
        elif char not in seen:
            result += char
    return result