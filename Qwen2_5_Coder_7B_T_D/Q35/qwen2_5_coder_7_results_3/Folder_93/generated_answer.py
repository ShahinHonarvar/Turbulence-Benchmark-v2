def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(58, 85):
        count[ord(s[i])] += 1
    return ''.join([char for char in s if (count[ord(char)] == 0 or 57 < ord(char) < 85) and s.index(char) != i for i in range(58, 85)])