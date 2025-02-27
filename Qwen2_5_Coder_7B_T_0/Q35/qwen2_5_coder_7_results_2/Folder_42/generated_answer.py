def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(18, 60):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or 18 <= s.index(char) < 18 or 60 <= s.rindex(char) < 60:
            result.append(char)
    return ''.join(result)