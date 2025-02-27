def remove_repeat_chars(s):
    target_range = s[73:84]
    unique_chars = set(target_range)
    result = []
    for char in s:
        if char in unique_chars:
            if result and char == result[-1] and (s.index(char) not in range(73, 84)):
                continue
            result.append(char)
    return ''.join(result)