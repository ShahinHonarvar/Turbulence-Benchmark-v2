def remove_repeat_chars(s):
    repeat_chars = [s[i] for i in range(70, 97) if s.count(s[i]) > 1]
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)