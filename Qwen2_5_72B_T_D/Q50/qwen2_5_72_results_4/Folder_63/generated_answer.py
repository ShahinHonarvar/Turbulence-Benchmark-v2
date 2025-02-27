from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_counts = Counter((''.join(sorted(word)) for word in words if len(word) >= 3))
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 89