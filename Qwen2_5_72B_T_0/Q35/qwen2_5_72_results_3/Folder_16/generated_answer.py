def remove_repeat_chars(s):
    char_count = {}
    for i in range(91, 97):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or not 91 <= s.index(char) <= 96]
    return ''.join(result)