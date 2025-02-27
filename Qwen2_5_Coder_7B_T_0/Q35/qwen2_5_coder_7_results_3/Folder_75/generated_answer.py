def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(20, 51):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or not 20 < s.index(char) < 51:
            result.append(char)
    return ''.join(result)