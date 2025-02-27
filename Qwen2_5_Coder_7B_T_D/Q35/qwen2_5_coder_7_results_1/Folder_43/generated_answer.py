def remove_repeat_chars(s):
    count = [0] * 128
    for i in range(10, 28):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] < 2 or not 10 < s.index(char) < 28:
            result.append(char)
    return ''.join(result)