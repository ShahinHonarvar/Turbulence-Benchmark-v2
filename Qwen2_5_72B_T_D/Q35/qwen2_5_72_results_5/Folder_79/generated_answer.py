def remove_repeat_chars(s):
    count = {}
    for i in range(2, 7):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [char for char in s if char not in count or count[char] == 1]
    return ''.join(result)