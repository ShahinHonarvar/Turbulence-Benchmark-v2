def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for i, char in enumerate(s[21:199]):
        if char not in unique_chars:
            if s.count(char, i, i + 1) + s.count(char, i + 1, len(s)) == 1:
                result.append(char)
                unique_chars.add(char)
    return ''.join(result)