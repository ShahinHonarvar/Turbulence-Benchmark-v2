def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(17, 87):
        count[ord(s[i])] += 1
    result = ''
    for char in s:
        if count[ord(char)] < 2 or (not 16 < s.index(char) < 87 and (not 16 < s.rindex(char) < 87)):
            result += char
    return result