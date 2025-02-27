from collections import defaultdict

def remove_repeat_chars(s):
    char_count = defaultdict(int)
    for i in range(44, 67):
        if i < len(s):
            char_count[s[i]] += 1
    result = []
    for char in s:
        if char_count[char] < 2:
            result.append(char)
    return ''.join(result)