def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 48 < s.index(char) < 76:
            if char not in seen:
                seen.add(char)
                result.append(char)
            else:
                result = [c for c in result if c != char]
    return ''.join(result)