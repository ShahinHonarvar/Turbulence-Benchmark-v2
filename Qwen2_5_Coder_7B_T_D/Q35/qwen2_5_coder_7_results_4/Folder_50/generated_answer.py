def remove_repeat_chars(s):
    counts = [0] * 256
    for i in range(13, 76):
        counts[ord(s[i])] += 1
    return ''.join([char for char in s if counts[ord(char)] < 2 or char in s[:13] or char in s[76:]])