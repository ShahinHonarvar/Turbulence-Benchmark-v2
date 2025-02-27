def remove_repeat_chars(s):
    count = {}
    for i in range(20, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    return ''.join([c for c in s if count[c] <= 1])