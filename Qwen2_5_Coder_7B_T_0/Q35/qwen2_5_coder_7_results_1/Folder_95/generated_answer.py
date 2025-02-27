def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 32 < ord(char) < 99:
            if char not in seen:
                seen.add(char)
                result.append(char)
            else:
                result = [c for c in result if c != char]
    return ''.join(result)