def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(307, 807):
        count[ord(s[i])] += 1
    new_s = []
    for i in range(len(s)):
        if count[ord(s[i])] == 1 or i < 306 or i >= 807:
            new_s.append(s[i])
    return ''.join(new_s)