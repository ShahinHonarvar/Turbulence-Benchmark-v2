from collections import Counter

def remove_repeat_chars(s):
    chars = s[20:51]
    char_count = Counter(chars)
    unique_chars = [ch for ch in char_count if char_count[ch] == 1]
    result = s[:20] + ''.join([ch for ch in chars if ch in unique_chars]) + s[51:]
    return result