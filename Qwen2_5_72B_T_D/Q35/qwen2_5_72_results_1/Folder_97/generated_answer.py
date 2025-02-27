from collections import Counter

def remove_repeat_chars(s):
    counter = Counter(s[34:69])
    return ''.join((char for char in s if char not in counter or counter[char] == 1))