def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(11, 76):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or not 11 < s.index(char) < 76:
            result.append(char)
    return ''.join(result)