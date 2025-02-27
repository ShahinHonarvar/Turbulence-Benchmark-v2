from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_dict = Counter((''.join(sorted(word)) for word in strings if len(word) >= 3))
    pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs >= 65