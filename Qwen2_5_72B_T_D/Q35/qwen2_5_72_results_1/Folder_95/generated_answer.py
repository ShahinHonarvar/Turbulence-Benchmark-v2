def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, len(s) - 1):
        if 32 < ord(s[i]) < 99:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    result = ''.join([char for char in s if char_count.get(char, 0) <= 1 or not 32 < ord(char) < 99])
    return result