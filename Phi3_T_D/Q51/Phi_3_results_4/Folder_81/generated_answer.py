from collections import Counter

def if_contains_anagrams(strings):

    def count_chars(s):
        return Counter((c.lower() for c in s if c.isalpha()))
    anagrams = {}
    for s in strings:
        char_count = frozenset(count_chars(s).items())
        if char_count in anagrams:
            anagrams[char_count].append(s)
        else:
            anagrams[char_count] = [s]
    count_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) >= 2))
    if count_pairs > 79:
        return False
    return True