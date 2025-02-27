def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(10, 80):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or not 10 < s.index(char) < 80:
            result.append(char)
    return ''.join(result)