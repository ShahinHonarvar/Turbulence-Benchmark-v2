from collections import Counter

def remove_repeat_chars(s):
    substring = s[18:60]
    freq = Counter(substring)
    to_remove = {char for char, count in freq.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or not 18 <= s.index(char) < 60))
    return result