from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_counts[normalized] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 47