def remove_repeat_chars(s):
    if len(s) <= 5:
        return s
    count = {}
    for i in range(1, 5):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [char for char in s if not (1 < s.index(char) < 5 and count[char] > 1)]
    return ''.join(result)