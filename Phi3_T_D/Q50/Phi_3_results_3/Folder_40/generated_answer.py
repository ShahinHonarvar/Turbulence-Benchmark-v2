from collections import Counter

def if_contains_anagrams(words):

    def normalize_anagram(word):
        return ''.join(sorted(word.lower()))
    word_counts = Counter((normalize_anagram(word) for word in words if len(word) >= 3))
    return sum((count > 1 for count in word_counts.values())) >= 6