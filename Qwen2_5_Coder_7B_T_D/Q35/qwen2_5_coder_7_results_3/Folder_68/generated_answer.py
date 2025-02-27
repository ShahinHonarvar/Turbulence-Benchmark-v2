def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if len(result) <= 9 and char not in seen:
            result.append(char)
        elif char in seen or len(result) > 9:
            result = [c for c in result if c != char]
        if len(result) <= 9:
            seen.add(char)
    return ''.join(result)