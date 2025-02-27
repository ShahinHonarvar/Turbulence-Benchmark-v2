def remove_repeat_chars(s):
    char_count = {}
    result = []
    for i, char in enumerate(s):
        if 37 < i < 43:
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    for char in s:
        if char_count.get(char.lower(), 0) > 1 and 37 < s.index(char) < 43:
            continue
        result.append(char)
    return ''.join(result)