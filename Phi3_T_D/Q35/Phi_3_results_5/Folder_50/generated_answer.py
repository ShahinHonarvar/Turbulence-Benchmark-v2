def remove_repeat_chars(s):
    start, end = (13, 77)
    seen = {}
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        else:
            result.append(char)
    for char in result:
        if seen.get(char, 0) > 1:
            result = [c for c in result if c != char]
    return ''.join(result)