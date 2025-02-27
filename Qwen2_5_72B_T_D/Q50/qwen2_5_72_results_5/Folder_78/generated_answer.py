from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in words]
    anagram_counts = Counter(sorted_words)
    pairs = 0
    for count in anagram_counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 79