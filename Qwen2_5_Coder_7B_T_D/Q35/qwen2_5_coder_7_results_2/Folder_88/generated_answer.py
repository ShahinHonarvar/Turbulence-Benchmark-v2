def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(3, 9):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 1 or (3 <= s.index(char) <= 9 and count[ord(char)] > 1):
            result.append(char)
    return ''.join(result)