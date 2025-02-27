def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(38, 81):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] < 2 or not 38 < ord(char) < 81:
            result.append(char)
    return ''.join(result)