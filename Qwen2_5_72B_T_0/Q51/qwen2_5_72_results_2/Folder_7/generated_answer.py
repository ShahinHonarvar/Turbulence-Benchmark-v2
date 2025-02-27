from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_counts = Counter((''.join(sorted(s)) for s in strings))
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_of_anagrams <= 445