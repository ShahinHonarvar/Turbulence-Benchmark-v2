from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in words]
    anagram_counts = Counter(sorted_words)
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 69