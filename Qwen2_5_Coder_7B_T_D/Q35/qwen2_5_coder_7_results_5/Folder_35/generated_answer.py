def remove_repeat_chars(s):
    seen = set()
    result = ''
    for char in s:
        if 77 < s.index(char) < 84:
            if char not in seen:
                seen.add(char)
                result += char
    return result