from collections import Counter

def if_contains_anagrams(strings):
    normalized = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    count = Counter(normalized)
    anagram_pairs = sum((freq * (freq - 1) // 2 for freq in count.values()))
    return anagram_pairs >= 10