def remove_repeat_chars(s):
    count = {}
    for i in range(71, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    return ''.join([char for char in s if (char not in count or count[char] == 1) and (i < 70 or i >= 200)])