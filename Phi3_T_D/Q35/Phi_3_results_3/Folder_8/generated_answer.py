def remove_repeat_chars(s):
    count = {}
    for i in range(45, 49):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [char for i, char in enumerate(s) if char not in count or (char in count and count[char] == 1) or 45 <= i <= 48]
    return ''.join(result)