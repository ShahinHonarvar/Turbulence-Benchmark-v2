from collections import Counter

def if_contains_anagrams(words):
    norm_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    count = Counter(norm_words)
    anagram_pairs = sum((n * (n - 1) // 2 for n in count.values() if n > 1))
    return anagram_pairs >= 88