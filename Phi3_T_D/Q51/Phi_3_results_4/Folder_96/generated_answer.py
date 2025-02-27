from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    sorted_words = [''.join(sorted(word)) for word in words if len(word) >= 3]
    frequency = Counter(sorted_words)
    anagram_pairs = sum((val > 1 for val in frequency.values()))
    return anagram_pairs <= 4