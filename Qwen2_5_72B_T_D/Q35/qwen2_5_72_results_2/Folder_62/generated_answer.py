from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[50:92])
    repeated_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 50 <= s.index(char) < 92))
    return result