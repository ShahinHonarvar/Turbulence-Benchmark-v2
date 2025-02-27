def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(30, 200):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if 30 <= s.find(char) < 200 and count[ord(char)] > 1:
            count[ord(char)] = 0
        if count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)