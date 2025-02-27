def remove_repeat_chars(s):
    seen = set()
    result = ''
    for char in s:
        if char not in seen:
            if s.count(char) <= 1 or s.index(char) < 2 or s.index(char) > 7:
                result += char
            elif s.index(char) == 1:
                seen.add(char)
            elif s.index(char) == 7:
                seen.add(char)
    return result