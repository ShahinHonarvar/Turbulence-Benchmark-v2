def remove_repeat_chars(s):
    count = {}
    for i in range(126, 825):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for char, cnt in count.items():
        if cnt > 1:
            s = s.replace(char, '')
    return s