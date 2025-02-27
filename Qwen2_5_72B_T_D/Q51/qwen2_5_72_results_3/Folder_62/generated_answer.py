from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    valid_words = [word for word in words if len(word) >= 3 and word.isalpha()]
    anagram_counts = Counter((normalize(word) for word in valid_words))
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 289