def remove_repeat_chars(s):
    chars = {}
    for i in range(36, 52):
        if i < len(s):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
    result = ''.join([char for char in s if chars.get(char, 0) <= 1 or s.index(char) < 36 or s.index(char) > 51])
    return result