def remove_repeat_chars(s):
    count = {}
    for i in range(28, 96):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    result = [c for c in s if c not in count or count[c] <= 1]
    return ''.join(result)