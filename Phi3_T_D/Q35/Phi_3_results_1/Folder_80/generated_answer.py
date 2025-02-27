def remove_repeat_chars(s):
    char_to_remove = set()
    start, end = (57, 84)
    for i in range(start, end):
        char = s[i]
        if s.count(char, start, end) > 1:
            char_to_remove.add(char)
    result = [c for c in s if c not in char_to_remove or start <= s.index(c) < end or c == char_to_remove.pop()]
    return ''.join(result)