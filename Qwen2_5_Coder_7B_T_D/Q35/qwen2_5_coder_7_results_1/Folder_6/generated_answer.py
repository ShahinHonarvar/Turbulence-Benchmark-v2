def remove_repeat_chars(s):
    seen = [0] * 256
    result = []
    for char in s:
        if 20 < s.index(char) < 93:
            seen[ord(char)] += 1
    for char in s:
        if 20 < s.index(char) < 93 and seen[ord(char)] == 1 or (20 >= s.index(char) or 93 <= s.index(char)):
            result.append(char)
    return ''.join(result)