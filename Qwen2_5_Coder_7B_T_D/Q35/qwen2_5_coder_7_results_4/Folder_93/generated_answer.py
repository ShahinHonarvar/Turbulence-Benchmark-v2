def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(57, 85):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or (count[ord(char)] > 1 and (not 57 < ord(char) < 85)):
            result.append(char)
    return ''.join(result)