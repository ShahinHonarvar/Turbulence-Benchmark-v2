from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word)).lower()
    normalized_words = Counter([normalize(word) for word in words if len(word) >= 3])
    return sum((value > 1 for value in normalized_words.values())) >= 43