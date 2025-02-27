def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(13, 91):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or (13 <= s.index(char) <= 91 and s.count(char) == 1):
            result.append(char)
    return ''.join(result)