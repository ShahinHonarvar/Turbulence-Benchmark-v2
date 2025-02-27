from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    filtered_words = [normalize(word) for word in words if len(word) >= 3]
    anagram_counts = Counter(filtered_words)
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 67