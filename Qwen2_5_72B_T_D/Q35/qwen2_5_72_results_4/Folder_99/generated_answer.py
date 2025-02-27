from collections import Counter

def remove_repeat_chars(s):
    freq = Counter(s[450:905])
    result = [char for char in s if freq[char] <= 1 or s.index(char) < 450 or s.index(char) >= 905]
    return ''.join(result)