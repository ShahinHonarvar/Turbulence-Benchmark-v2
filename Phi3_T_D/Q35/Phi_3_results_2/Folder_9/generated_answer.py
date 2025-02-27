from collections import Counter

def remove_repeat_chars(s):
    substring = s[80:200]
    counts = Counter(substring)
    result = [c for i, c in enumerate(s) if c not in counts or counts[c] == 1]
    result.extend((substring[i] for i, c in enumerate(substring) if counts[c] == 1))
    return ''.join(result)