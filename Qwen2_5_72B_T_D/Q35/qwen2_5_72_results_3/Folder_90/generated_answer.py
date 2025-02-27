from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 306 or len(s) <= 807:
        return s
    substring = s[306:807]
    freq = Counter(substring)
    to_remove = {char for char, count in freq.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result