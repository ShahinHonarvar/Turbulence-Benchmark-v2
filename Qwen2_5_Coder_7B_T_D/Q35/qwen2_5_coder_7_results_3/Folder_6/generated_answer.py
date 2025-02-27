def remove_repeat_chars(s):
    count = [0] * 128
    for i in range(20, 93):
        count[ord(s[i])] += 1
    return ''.join([char for char in s if count[ord(char)] == 0 or (char not in s[20:93] or count[ord(char)] == 1)])