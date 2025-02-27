def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(14, 91):
        count[ord(s[i])] += 1
    return ''.join([c for c in s if count[ord(c)] == 0 or s.index(c) < 14 or s.rindex(c) > 91])