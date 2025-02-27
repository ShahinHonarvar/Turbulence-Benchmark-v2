def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(46, 91):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (ord(char) < 46 or ord(char) > 91) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)