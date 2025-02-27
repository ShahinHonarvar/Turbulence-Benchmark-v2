def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(356, 988):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or not 355 < s.index(char) < 988:
            result.append(char)
    return ''.join(result)